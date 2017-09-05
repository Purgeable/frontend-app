"""This module allows running development server."""
import config
from apps import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=config.DEBUG)
