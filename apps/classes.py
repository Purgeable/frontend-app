import pandas as pd
from urllib import request

class CSVFile(object):
    """Class that controls a CSV file."""
    def __init__(self, filename, dirname='files'):
        self.filename = filename
        self.dirname = dirname
        self.url = 'https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/%s' % \
            filename

    def _open_local(self, mode):
        """Return a local file instance."""
        return open("%s/%s" % (self.dirname, self.filename), mode)

    def update(self):
        """Update a local copy with the latest content from the main
        GitHub repository.
        """
        with self._open_local('w') as csv:
            data = request.urlopen(self.url).read().decode('utf-8')
            csv.write(data)

    def get_contents(self):
        """Return contents of a local copy."""
        with self._open_local('r') as csv:
            contents = csv.read()
        return contents

class DataFrame(object):
    """Class that manipulates a pandas dataframe."""
    def _make_url(self, freq):
        url = "https://raw.githubusercontent.com/epogrebnyak/mini-kep/master/data/processed/latest/{}"
        filename = "df{}.csv".format(freq)
        return url.format(filename)

    def get_from_repo(self, freq):
        """Suggested code to read pandas dataframes from 'mini-kep'
        stable URL.
        """
        url = self._make_url(freq)
        return self.read_csv(url)

    def read_csv(self, source):
        """Canonical wrapper for pd.read_csv(). Treats first column at
        time index.

        Returns:
            pd.DataFrame()
        """
        converter_arg = dict(converters={0: pd.to_datetime}, index_col=0)
        return pd.read_csv(source, **converter_arg)
