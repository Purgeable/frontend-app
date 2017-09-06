from urllib import request

class CSVFile(object):
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
            csv.close()

    def get_contents(self):
        """Return contents of a local copy."""
        with self._open_local('r') as csv:
            contents = csv.read()
            csv.close()
        return contents
