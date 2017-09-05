from flask import Blueprint

# Define the blueprint for this application
main = Blueprint('main', __name__)

@main.route('/')
def fetch_csv():
    raise Exception("it works!")
