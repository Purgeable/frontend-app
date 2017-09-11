"""This is the main entrypoint for all apps. In this module we
initialize global instances of various packages.
"""
import os

from flask import Flask
from coverage import Coverage

# Start gathering code coverage
cov = Coverage()
cov.start()

# Create new Flask app that will be used as main entrypoint
app = Flask(__name__)
app.config.from_object('config')

# Register app blueprints
from apps.views import main
app.register_blueprint(main, url_prefix='')

# Save code coverage data and render a GitHub badge
cov.stop()
cov.save()
os.system('coverage-badge -f -o apps/static/img/coverage.svg')
