import unittest
import config

from urllib.parse import urljoin
from flask import url_for
from apps import app
from apps.classes import DataFrame

class HomeTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            self.url = urljoin(config.HOST_URL, url_for('main.home'))
            client = app.test_client()
            self.response = client.get(self.url)
            self.data = self.response.get_data(as_text=True)

    def test_body(self):
        assert self.response.status_code == 200
        assert isinstance(self.data, str)

class AnnualTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            self.url = urljoin(config.HOST_URL, url_for('main.annual'))
            client = app.test_client()
            self.response = client.get(self.url)
            self.data = self.response.get_data(as_text=True)

    def test_body(self):
        assert self.response.status_code == 200
        assert isinstance(self.data, str)

    def test_json(self):
        df = DataFrame()
        csv_data = df.read_csv(self.url)
        assert not csv_data.empty

class QuarterlyTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            self.url = urljoin(config.HOST_URL, url_for('main.quarterly'))
            client = app.test_client()
            self.response = client.get(self.url)
            self.data = self.response.get_data(as_text=True)

    def test_body(self):
        assert self.response.status_code == 200
        assert isinstance(self.data, str)

    def test_json(self):
        df = DataFrame()
        csv_data = df.read_csv(self.url)
        assert not csv_data.empty

class MonthlyTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            self.url = urljoin(config.HOST_URL, url_for('main.monthly'))
            client = app.test_client()
            self.response = client.get(self.url)
            self.data = self.response.get_data(as_text=True)

    def test_body(self):
        assert self.response.status_code == 200
        assert isinstance(self.data, str)

    def test_json(self):
        df = DataFrame()
        csv_data = df.read_csv(self.url)
        assert not csv_data.empty
