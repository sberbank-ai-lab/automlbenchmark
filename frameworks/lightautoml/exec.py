import logging
import os

import pandas as pd
import numpy as np
import torch
from sklearn.metrics import log_loss, roc_auc_score

from amlb.benchmark import TaskConfig
from amlb.data import Dataset
from amlb.utils import dir_of, run_cmd, Timer
from amlb.results import save_predictions_to_file

from frameworks.shared.callee import call_run, result, output_subdir
from lightautoml.tasks import Task
from lightautoml.automl.presets.tabular_presets import TabularAutoML, TabularUtilizedAutoML

log = logging.getLogger(__name__)


def get_automl(is_binary, config):
    logging.debug('Create task...')
    task = Task('binary') if is_binary else Task('multiclass')
    logging.debug('Task created')

    automl = TabularUtilizedAutoML(task=task, timeout=config.max_runtime_seconds, random_state=config.seed)

    return automl


def run(dataset: Dataset, config: TaskConfig):
    log.info("\n**** lightautoml (R) ****\n")

    y_train, y_test = dataset.train.y_enc, dataset.test.y_enc

    is_binary = True

    if config.type == 'classification':
        is_binary = True if len(set(y_train)) < 3 else False

    log.info("Environment: %s", os.environ)

    automl = get_automl(is_binary, config)
    torch.set_num_threads(config.cores)
    np.random.seed(config.seed)

    df_train = pd.DataFrame(
        dataset.train.data,
        columns=map(
            lambda x: x.name,
            sorted(dataset.features, key=lambda x: x.index, reverse=False)
        )
    )
    log.info("df_train is initialized. Shape: {}".format(df_train.shape))

    df_train[dataset.target.name] = y_train

    log.info("Start training.")

    # fit
    with Timer() as training:

        oof_pred = automl.fit_predict(train_data=df_train, roles={'target': dataset.target.name}).data

    log.info("Predicting on the test set.")
    df_test = pd.DataFrame(
        dataset.test.data,
        columns=map(
            lambda x: x.name,
            sorted(dataset.features, key=lambda x: x.index, reverse=False)
        )
    )
    df_test[dataset.target.name] = y_test
    #    y_test = dataset.test.data

    probabilities = automl.predict(df_test).data

    if probabilities is not None:
        if is_binary:
            probabilities = np.vstack([
                1 - probabilities[:, 0], probabilities[:, 0]
            ]).T

    if is_binary:
        oof_pred = oof_pred[:, 0]
        flags = ~np.isnan(oof_pred)
        y_oof = y_train[flags]

        oof_score = roc_auc_score(
            y_oof,
            oof_pred[flags]
        )
    else:
        flags = (np.isnan(oof_pred).sum(axis=1) == 0)

        oof_score = log_loss(
            y_train[flags],
            oof_pred[flags, :]
        )

    log.debug(probabilities)
    log.debug(config.output_predictions_file)
    log.debug('OOF score: {}'.format(oof_score))

    save_predictions_to_file(dataset=dataset,
                             output_file=config.output_predictions_file,
                             probabilities=probabilities,
                             target_is_encoded=True,
                             predictions=np.argmax(probabilities, axis=1),
                             truth=y_test)

    return dict(
        oof_score=oof_score,
        models_count=1,
        training_duration=training.duration
    )


if __name__ == '__main__':
    call_run(run)

