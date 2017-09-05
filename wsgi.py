"""WSGI entrypoint to execute Gunicorn from."""
from apps import app

if __name__ == '__main__':
    app.run()
