import sklearn
import sklearn.svm
from sklearn import tree
import numpy as np


class SvmClassifier(sklearn.svm.SVC):
    pass
    # created for the sake of consistency


class AnnClassifier(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    # TODO: implement ANN
    def fit(self, X, y):
        pass

    def transform(self, X):
        pass


class DecisionTreeClassifier(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):


    model = []

    def __init__(self):
        self.model = tree.DecisionTreeClassifier()

    def fit(self, X, y):
        self.model.fit(X,y)

    def transform(self, X):
        return self.model.predict(X)


def classify_projects(projects, model, feature_extractor):

    for project in projects:
        feature_vectors = [feature_extractor.get_feature_vector(code) for code in project.codes]
        predictions = model.predict(feature_vectors)
        predicted_label = np.argmax(np.bincount(predictions))
        yield predicted_label
