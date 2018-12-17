import data_management
import feature_extraction
#import classification

# loading data
data_manager = data_management.CsvLoader("data.csv")
code_files_grouped_by_project = data_manager.get_projects_list()

training_to_test_ratio = 0.2
training_set, test_set = data_management.split_to_test_and_training(code_files_grouped_by_project, training_to_test_ratio)

training_codes = [code for proj in code_files_grouped_by_project for code in proj.codes]
feature_extractor = feature_extraction.FeatureExtractor(training_codes)
feature_matrix = [feature_extractor.get_feature_vector(data_vector.code) for data_vector in training_set]
pass