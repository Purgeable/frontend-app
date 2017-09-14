import unittest
import config

class ProductionConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.config = config.ProductionConfig

    def test_debug(self):
        assert hasattr(self.config, 'DEBUG')
        assert isinstance(self.config.DEBUG, bool)
        assert not self.config.DEBUG

    def test_host_url(self):
        assert hasattr(self.config, 'HOST_URL')
        assert isinstance(self.config.HOST_URL, str)
        assert self.config.HOST_URL.startswith('http')
        assert not self.config.HOST_URL.endswith('/')

    def test_base_dir(self):
        assert hasattr(self.config, 'BASE_DIR')
        assert self.config.BASE_DIR.endswith('/frontend-app')

    def test_threads_per_page(self):
        assert hasattr(self.config, 'THREADS_PER_PAGE')
        assert isinstance(self.config.THREADS_PER_PAGE, int)

    def test_csrf_enabled(self):
        assert hasattr(self.config, 'CSRF_ENABLED')
        assert isinstance(self.config.CSRF_ENABLED, bool)
        assert self.config.CSRF_ENABLED

    def test_csrf_session_key(self):
        assert hasattr(self.config, 'CSRF_SESSION_KEY')
        assert isinstance(self.config.CSRF_SESSION_KEY, str)
        assert self.config.CSRF_SESSION_KEY.isalnum()

    def test_secret_key(self):
        assert hasattr(self.config, 'SECRET_KEY')
        assert isinstance(self.config.SECRET_KEY, str)
        assert self.config.SECRET_KEY.isalnum()

class DevelopmentConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.config = config.DevelopmentConfig

    def test_debug(self):
        assert hasattr(self.config, 'DEBUG')
        assert isinstance(self.config.DEBUG, bool)
        assert self.config.DEBUG

    def test_host_url(self):
        assert hasattr(self.config, 'HOST_URL')
        assert isinstance(self.config.HOST_URL, str)
        assert self.config.HOST_URL.startswith('http')
        assert not self.config.HOST_URL.endswith('/')

    def test_base_dir(self):
        assert hasattr(self.config, 'BASE_DIR')
        assert self.config.BASE_DIR.endswith('/frontend-app')

    def test_threads_per_page(self):
        assert hasattr(self.config, 'THREADS_PER_PAGE')
        assert isinstance(self.config.THREADS_PER_PAGE, int)

    def test_csrf_enabled(self):
        assert hasattr(self.config, 'CSRF_ENABLED')
        assert isinstance(self.config.CSRF_ENABLED, bool)
        assert self.config.CSRF_ENABLED

    def test_csrf_session_key(self):
        assert hasattr(self.config, 'CSRF_SESSION_KEY')
        assert isinstance(self.config.CSRF_SESSION_KEY, str)
        assert self.config.CSRF_SESSION_KEY.isalnum()

    def test_secret_key(self):
        assert hasattr(self.config, 'SECRET_KEY')
        assert isinstance(self.config.SECRET_KEY, str)
        assert self.config.SECRET_KEY.isalnum()

class DataSourceConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.config = config.DataSourceConfig

    def test_base_url(self):
        assert hasattr(self.config, 'BASE_URL')
        assert isinstance(self.config.BASE_URL, str)
        assert self.config.BASE_URL.startswith('http')
        assert not self.config.BASE_URL.endswith('/')

    def test_csv_files(self):
        assert hasattr(self.config, 'CSV_FILES')
        assert isinstance(self.config.CSV_FILES, tuple)
        assert 'dfa.csv' in self.config.CSV_FILES
        assert 'dfm.csv' in self.config.CSV_FILES
        assert 'dfq.csv' in self.config.CSV_FILES
