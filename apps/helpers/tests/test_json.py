import os.path
import unittest

from datetime import datetime
from apps.helpers.json import to_json, from_json

class JSONTestCase(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'status_test.json'
        self.date_format = '%Y-%m-%d %H:%M:%S'

    def test_from_json(self):
        data = from_json('status.json')
        assert isinstance(data, dict)
        assert 'timestamp' in data
        assert datetime.strptime(data['timestamp'], self.date_format)
        assert 'is_updated_ok' in data
        assert isinstance(data['is_updated_ok'], bool)

    def test_to_json(self):
        data = {
            'timestamp': datetime.now().strftime(self.date_format),
            'is_updated_ok': True
        }
        to_json(data, self.test_filename)
        assert os.path.isfile(self.test_filename)
        read_data = from_json(self.test_filename)
        assert data == read_data

    def tearDown(self):
        try:
            os.remove(self.test_filename)
        except OSError:
            pass
