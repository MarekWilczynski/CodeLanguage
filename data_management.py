import csv
import collections
from enum import Enum, auto
import numpy


class ProjectData(object):
    language = []
    codes = []

class CsvLoader(object):

    _file_handle = []
    _file = []

    def __init__(self, path="data.csv"):
        self._file = open(path)
        self._file_handle = csv.reader(self._file, delimiter=',')

    def next(self):
        return self._file_handle.__next__()

    def __next__(self):
        return self.next()

    def __iter__(self):
        return self

    def close(self):
        self._file.close()
        _file_handle = []
        _file = []

    def get_projects_list(self):
        codes, languages = zip(*self._generate_list())
        self.close()
        return codes, languages

    def _generate_list(self):
        project_id_column_index = 1
        code_column_index = 3
        language_column_index = 0

        self.next()  # skip first row
        first_row = self.next()
        project_id = first_row[project_id_column_index]
        code_list = [first_row[code_column_index]]
        language = first_row[language_column_index]
        language = language.replace("C++", "Cpp")
        for row in self:
            if (row[project_id_column_index] != project_id):
                yield code_list, Languages[language]
                project_id = row[project_id_column_index]
                language = row[language_column_index]
                language = language.replace("C++", "Cpp")
                code_list = []
            code_list.append(row[code_column_index])


def split_to_test_and_training(data, labels, ratio):
    # sklearn split could not be used, because collection of singletons is not a valid collection
    data_count = len(data)
    split_index = int(ratio * data_count)

    training_data, training_labels = data[:-split_index], labels[:-split_index]
    test_data, test_labels = data[:split_index], labels[:split_index]

    training_data, training_labels = zip(*flatten_project_data(training_data, training_labels))

    training_data = list(training_data)
    test_data = list(test_data)

    return training_data, training_labels, test_data, test_labels

def flatten_project_data(data, labels):
    # method creates a list with a label assigned to each code
    for codes, label in zip(data, labels):
        for code in codes:
            yield code, label


class Languages(Enum):
    # the enum could be dynamic. But it's not for the sake of easier job with the IDE.
    Swift = auto()
    Cpp = auto()
    Kotlin = auto()
    Scala = auto()
    Java = auto()
    Mathematica = auto()
    C = auto()
    Python = auto()
    Haskell = auto()
    Ruby = auto()
    Fortran = auto()
    MATLAB = auto()
    Perl = auto()
    Go = auto()
    R = auto()
    JavaScript = auto()
    PHP = auto()
    Rust = auto()
    Julia = auto()
