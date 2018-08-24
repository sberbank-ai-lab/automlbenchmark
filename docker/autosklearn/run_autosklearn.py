import sys

from autosklearn.classification import AutoSklearnClassifier
import autosklearn.metrics
import numpy as np
from sklearn.metrics import accuracy_score


sys.path.append('/bench/common')
import common_code

if __name__ == '__main__':
    runtime_seconds = int(sys.argv[1])
    number_cores = int(sys.argv[2])
    performance_metric = sys.argv[3]


    X_train, y_train = common_code.get_X_y_from_arff(common_code.TRAIN_DATA_PATH)
    X_test, y_test = common_code.get_X_y_from_arff(common_code.TEST_DATA_PATH)
    X_train, X_test = X_train.astype(float), X_test.astype(float)

    # Set resources based on datasize
    print('ignoring n_cores.')
    # If small data:
    if len(y_train) <= 20000:
        number_cores = 8
        ml_memory_limit = 16000 #16GB
    elif len(y_train) <= 200000:
        number_cores = 32
        ml_memory_limit = 64000 #64GB
    else:
        number_cores = 64
        ml_memory_limit = 640000 #64GB

    print('Running auto-sklearn with a maximum time of {}s on {} cores, optimizing {}.'
          .format(runtime_seconds, number_cores, performance_metric))

    print('Using meta-learned initialization, which might be bad (leakage).')
    auto_sklearn = AutoSklearnClassifier(time_left_for_this_task=runtime_seconds, \
        ml_memory_limit=ml_memory_limit)
    print('always optimize towards accuracy.')
    auto_sklearn.fit(X_train, y_train, metric=autosklearn.metrics.accuracy)
    # Convert output to strings for classification
    class_predictions = auto_sklearn.predict(X_test).astype(np.int_).astype(np.str_)
    class_probabilities = auto_sklearn.predict_proba(X_test)

    print('Optimization was towards metric, but following score is always accuracy:')
    print("Accuracy: " + str(accuracy_score(y_test, class_predictions)))  

    common_code.save_predictions_to_file(class_probabilities, class_predictions)
