import unittest
import urllib.request
import config

class HomeTestCase(unittest.TestCase):
    def setUp(self):
        self.response = urllib.request.urlopen(config.BASE_URL)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200

class AnnualTestCase(unittest.TestCase):
    def setUp(self):
        url = '%sannual' % config.BASE_URL
        self.response = urllib.request.urlopen(url)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200

class QuarterlyTestCase(unittest.TestCase):
    def setUp(self):
        url = '%squarterly' % config.BASE_URL
        self.response = urllib.request.urlopen(url)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200

class MonthlyTestCase(unittest.TestCase):
    def setUp(self):
        url = '%smonthly' % config.BASE_URL
        self.response = urllib.request.urlopen(url)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200
