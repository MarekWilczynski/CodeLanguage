import data_management
import feature_extraction
import classification

import sklearn
import sklearn.decomposition
import sklearn.svm
import sklearn.metrics
import sklearn.pipeline
from sklearn import tree

import numpy as np
from time import time


# loading data
t = time()
data_manager = data_management.CsvLoader("data.csv")
used_data_count = 9000  # this as much as my RAM can handle
code_files_grouped_by_project, project_labels = data_manager.get_projects_list()
code_files_grouped_by_project = code_files_grouped_by_project[:used_data_count]
project_labels = project_labels[:used_data_count]

print('Data loaded. Time elapsed: %.2f s' % (time() - t))
t = time()

# splitting data into training and test sets
training_to_test_ratio = 0.2
training_codes, training_labels, test_set, test_labels = data_management.split_to_test_and_training(
    code_files_grouped_by_project,
    project_labels,
    training_to_test_ratio)

# extracting features
feature_extractor = feature_extraction.FeatureExtractor(code_files_grouped_by_project)

print('Word dictionary completed. Time elapsed: %.2f s' % (time() - t))
t = time()

training_feature_matrix = np.array([feature_extractor.get_feature_vector(code) for code in training_codes])

print('Features extracted Time elapsed: %.2f s' % (time() - t))
t = time()

training_codes = []  # free memory
code_files_grouped_by_project = []  # free memory

# creating pipeline 
classifier = sklearn.svm.SVC(gamma='scale', kernel='linear')
estimators = [('pca', sklearn.decomposition.PCA(n_components=100)), ('classifier', classifier)]
# n_components found via gridsearch
pipeline = sklearn.pipeline.Pipeline(estimators)
classification_model = pipeline

# training
training_labels = [label_enum.value for label_enum in training_labels]
classification_model.fit(training_feature_matrix, training_labels)
training_feature_matrix = []  # free memory

print('Training finished. Time elapsed: %.2f s' % (time() - t))
t = time()

# testing on test data
predicted_labels = list(classification.classify_projects(test_set, classification_model, feature_extractor))

test_labels = [proj.value for proj in test_labels]
print("Accuracy: %f" % sklearn.metrics.accuracy_score(predicted_labels, test_labels))

