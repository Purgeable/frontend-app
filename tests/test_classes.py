import os
import unittest
import pandas as pd

from apps.classes import LocalFile, RemoteFile

CONVERTER_ARGS = dict(converters={0: pd.to_datetime}, index_col=0)

class LocalFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = LocalFile('dfa.csv')

    def test_attrs(self):
        assert os.path.exists(self.csv.path)
        assert self.csv.url == 'https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/dfa.csv'

    def test_update_from_parent_repo(self):
        self.csv.update_from_parent_repo()
        contents = pd.read_csv(self.csv.url, **CONVERTER_ARGS)
        assert not contents.empty

    def test_get_contents(self):
        contents = self.csv.get_contents()
        assert isinstance(contents, str)

class RemoveFileTestCase(unittest.TestCase):
    def setUp(self):
        self.csv = RemoteFile('dfm.csv')

    def test_attrs(self):
        assert self.csv.url == 'https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/dfm.csv'
