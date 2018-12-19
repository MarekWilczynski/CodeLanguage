import data_management
import feature_extraction
import classification

import sklearn
import sklearn.decomposition
import sklearn.svm
import sklearn.metrics
import sklearn.pipeline
from sklearn import tree

import classification
import numpy as np

# loading data
data_manager = data_management.CsvLoader("data.csv")
code_files_grouped_by_project = data_manager.get_projects_list()
code_files_grouped_by_project = code_files_grouped_by_project[:9000]

# splitting data into training and test sets
training_to_test_ratio = 0.2
training_set, test_set = data_management.split_to_test_and_training(code_files_grouped_by_project,
                                                                    training_to_test_ratio)
# extracting features
feature_extractor = feature_extraction.FeatureExtractor(code_files_grouped_by_project)
training_feature_matrix = np.array(
    [feature_extractor.get_feature_vector(data_vector.code) for data_vector in training_set])

training_labels = [data_set.language.value for data_set in training_set]
training_set = []  # free memory
code_files_grouped_by_project = []  # free memory

# creating pipeline 
classifier = sklearn.svm.SVC(gamma='scale', kernel='linear')
estimators = [('pca', sklearn.decomposition.PCA()), ('classifier', classifier)]
pipeline = sklearn.pipeline.Pipeline(estimators)

# gridsearch initialization
param_grid = dict(pca__n_components=[100])
classification_model = sklearn.model_selection.GridSearchCV(pipeline, param_grid=param_grid, cv=5, verbose=1, n_jobs=1)

# training
classification_model.fit(training_feature_matrix, training_labels)
training_feature_matrix = []  # free memory

print('Best estimator: %s' % str(classification_model.best_estimator_))
print('Best index: %s' % str(classification_model.best_index_))
print('Best params: %s' % str(classification_model.best_params_))
print('Best score: %s' % str(classification_model.best_score_))

# testing on test data
predicted_labels = list(classification.classify_projects(test_set, classification_model, feature_extractor))

correct_labels = [proj.language.value for proj in test_set]
print("Accuracy: %f" % sklearn.metrics.accuracy_score(predicted_labels, correct_labels))

