import json
import unittest
import pandas as pd
import config

from datetime import date
from urllib.parse import urljoin
from flask import url_for
from apps import app
from apps.views import check_csv_identity

class IdentityTestCase(unittest.TestCase):
    def setUp(self):
        with app.test_request_context():
            self.url = urljoin(config.HOST_URL, url_for('main.check_status'))
            self.response = app.test_client().get(self.url)
            data = self.response.get_data(as_text=True)
            self.json_data = json.loads(data)

    def test_identity(self):
        assert check_csv_identity()

    def test_status_json(self):
        assert isinstance(self.json_data, dict)
        current_year = date.today().year
        year = pd.to_datetime(self.json_data['timestamp']).year
        assert year >= current_year # generally, today or after
        assert self.json_data['is_updated_ok']
