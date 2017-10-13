import csv
import json
from apps import app
import unittest

class TimeSeriesApiInterfaceTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # FIXME: may parametrise this tests to add several more checks for various tricky urls, and another tests for invalid URLs    
    def test_valid_api_request_should_return_csv(self):
        csv_text = str(self.app.get('/oil/series/BRENT/d/2015/2017/').data)
        assert '2015-01-27,46.55\\n' in csv_text

    def test_invalid_api_request_should_return_json_error(self):
        response = self.app.get('/oil/series/BRENT/d/invalid/params/')
        assert response.status_code == 400
        assert 'message' in json.loads(response.data).keys()

    def test_url_with_invalid_time_range(self):
        # when end_date is less than start_date
        response = self.app.get('/oil/series/BRENT/d/2015/2010/')
        assert response.status_code == 400
        assert 'message' in json.loads(response.data).keys()