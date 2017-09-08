import json
import urllib.request
import unittest
import pandas as pd
import config

from datetime import date
from urllib.parse import urljoin
from flask import url_for
from apps import app
from apps.views import check_csv_identity

class IdentityTestCase(unittest.TestCase):
    def test_identity(self):
        assert check_csv_identity()

    def test_status_json(self):
        with app.test_request_context():
            url = urljoin(config.HOST_URL, url_for('main.check_status'))
            with urllib.request.urlopen(url) as data:
                status = json.loads(data.read().decode())
                assert isinstance(status, dict)
                current_year = date.today().year
                year = pd.to_datetime(status['timestamp']).year
                assert year >= current_year # generally, today or after
                assert status['is_updated_ok']
