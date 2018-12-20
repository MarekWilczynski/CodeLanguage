import numpy as np


def classify_projects(projects, model, feature_extractor):
# function too complex for unit testing
    for project in projects:
        feature_vectors = [feature_extractor.get_feature_vector(code) for code in project]
        predictions = model.predict(feature_vectors)
        predicted_label = np.argmax(np.bincount(predictions))
        yield predicted_label