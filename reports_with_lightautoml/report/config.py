
nfolds = 10
ff = '%.6g'
colormap = 'tab10'
# colormap = 'Set2'
# colormap = 'Dark2'

renamed_frameworks = dict()
excluded_frameworks = []

binary_result_label = 'AUC'
binary_score_label = 'AUC'
multiclass_result_label = 'logloss'
multiclass_score_label = 'neg. logloss'
regression_result_label = 'RMSE'
regression_score_label = 'neg. RMSE'

# impute_missing_with = 'constantpredictor'
impute_missing_with = 'randomforest'
# zero_one_refs = ('constantpredictor', 'tunedrandomforest')
zero_one_refs = ('constantpredictor', 'randomforest')

tasks_sort_by = 'nrows'

results_files = []
results_group = ''
