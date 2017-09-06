"""This is the main entrypoint for all apps. In this module we
initialize global instances of various packages.
"""
import os

from flask import Flask
from flask.ext.markdown import Markdown

# Create new Flask app that will be used as main entrypoint
app = Flask(__name__)
app.config.from_object('config')
Markdown(app)

# Register app blueprints
from apps.views import main
app.register_blueprint(main, url_prefix='')
