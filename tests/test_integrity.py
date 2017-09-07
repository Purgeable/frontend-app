import json
import urllib.request
import unittest
import pandas as pd
import config

from datetime import date
from urllib.parse import urljoin
from flask import url_for
from apps import app
from apps.classes import DataFrame

class IntegrityTestCase(unittest.TestCase):
    def test_integrity(self):
        with app.test_request_context():
            # read_csv() can read only absolute URLs
            sources = {
                'a': urljoin(config.HOST_URL, url_for('main.annual')),
                'q': urljoin(config.HOST_URL, url_for('main.quarterly')),
                'm': urljoin(config.HOST_URL, url_for('main.monthly'))
            }
            for freq, url in sources.items():
                df = DataFrame()
                df_repo = df.get_from_repo(freq)
                df_app = df.read_csv(url)
                assert df_repo.equals(df_app)

    def test_status_json(self):
        with app.test_request_context():
            url = urljoin(config.HOST_URL, url_for('main.check_status'))
            with urllib.request.urlopen(url) as data:
                status = json.loads(data.read().decode())
                assert isinstance(status, dict)
                assert status['pytest_exit_code'] == 0
                current_year = date.today().year
                year = pd.to_datetime(status['timestamp']).year
                assert year >= current_year # generally, today or after
                assert status['is_validated'] is True
