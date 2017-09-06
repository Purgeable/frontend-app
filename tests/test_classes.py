import unittest
from apps.classes import CSVFile

class CSVTestCase(unittest.TestCase):
    def setUp(self):
        self.csv_file = CSVFile('dfa.csv')

    def test_attrs(self):
        assert self.csv_file.filename == 'dfa.csv'
        assert self.csv_file.dirname == 'files'
        assert self.csv_file.url == 'https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/dfa.csv'

    def test_open_local(self):
        file_ = self.csv_file._open_local('r')
        assert hasattr(file_, 'read')
        file_.close()

    def test_get_contents(self):
        contents = self.csv_file.get_contents()
        assert isinstance(contents, str)
