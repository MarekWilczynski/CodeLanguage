import csv
import collections
from enum import Enum, auto
import numpy


class CsvLoader(object):

    _file_handle = []
    _file = []
    ProjectTuple = collections.namedtuple("ProjectTuple", "codes language")

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

    def get_projects_list(self):
        return list(self._generate_list())

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
                project_struct = self.ProjectTuple(codes=code_list, language=Languages[language])
                yield project_struct
                project_id = row[project_id_column_index]
                language = row[language_column_index]
                language = language.replace("C++", "Cpp")
                code_list = []
            code_list.append(row[code_column_index])

TrainingTuple = collections.namedtuple("TrainingTupleTuple", "code language")

def split_to_test_and_training(data, ratio):
    numpy.random.shuffle(data)
    training_data_size = int(len(data) * (1 - ratio))

    training_data = data[:training_data_size]
    test_data = data[:-training_data_size]

    training_data = list(flatten_project_data(training_data))
    return training_data, test_data


def flatten_project_data(data):
    for project in data:
        for code in project.codes:
            yield TrainingTuple(code, project.language)



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
