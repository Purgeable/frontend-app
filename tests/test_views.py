import unittest
import urllib.request
import config

from urllib.parse import urljoin
from flask import url_for
from apps import app

class HomeTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            url = urljoin(config.HOST_URL, url_for('main.home'))
        self.response = urllib.request.urlopen(url)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200

class AnnualTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            url = urljoin(config.HOST_URL, url_for('main.annual'))
        self.response = urllib.request.urlopen(url)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200

class QuarterlyTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            url = urljoin(config.HOST_URL, url_for('main.quarterly'))
        self.response = urllib.request.urlopen(url)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200

class MonthlyTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            url = urljoin(config.HOST_URL, url_for('main.monthly'))
        self.response = urllib.request.urlopen(url)

    def test_status_code(self):
        status_code = self.response.getcode()
        assert status_code == 200
