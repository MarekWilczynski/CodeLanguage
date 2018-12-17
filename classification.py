import sklearn


class SvmClassifier(sklearn.svm.SVC):
    pass
    # created for the sake of consistency


class AnnClassifier(sklearn.base.BaseEstimator, sklearn.base.TransformerMixin):
    # TODO: implement ANN
    def fit(self, X, y):
        pass

    def transform(self, X):
        pass