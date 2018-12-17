import sklearn
import abc


class Classifier(abc.ABC):
    model = []
    data_transformator = []

    def classify(self, data):
        return

    def start_training(self, data, labels):
        return


class SvmClassifier(Classifier):
    def __init__(self, data_transformator):
        self.model = sklearn.svm.SVC(kernel='linear')

    def start_training(self, data, labels):
        self.model.fit(data, labels)

    def classify(self, data):
        return self.model.predict(data)
