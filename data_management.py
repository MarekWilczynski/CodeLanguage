import csv
import collections
from enum import Enum, auto


class CsvLoader(object):

    file_handle = []
    file = []
    ProjectTuple = collections.namedtuple("ProjectTuple", "codes language")

    def __init__(self, path="data.csv"):
        self.file = open(path)
        self.file_handle = csv.reader(self.file, delimiter=',')


    def next(self):
        return self.file_handle.__next__()

    def __next__(self):
        return self.next()

    def __iter__(self):
        return self

    def close(self):
        self.file.close()

    def get_projects_list(self):
        project_list = []

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
            if(row[project_id_column_index] != project_id):
                project_struct = self.ProjectTuple(codes=code_list, language=Languages[language])
                project_list.append(project_struct)
                project_id = row[project_id_column_index]
                language = row[language_column_index]
                language = language.replace("C++", "Cpp")
                code_list = []
            code_list.append(row[code_column_index])
        return project_list


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
