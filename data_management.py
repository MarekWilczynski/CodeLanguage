import csv
import collections
class CsvLoader(object):

    file_handle = []
    file = []

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

    class ProjectIterator(object):
        iterator_handle = []
        ProjectTuple = collections.namedtuple("ProjectTuple", "code language")

        def __init__(self, csv_iterator):
            self.iterator_handle = csv_iterator

        def __next__(self):
            return self.next()

        def __iter__(self):
            return self

        def next(self):
            return self.file_handle.__next__()



class DataSet(object):


class ProjectData(object):
    __i