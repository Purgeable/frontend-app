from flask import Blueprint, render_template_string

# Define the blueprint for this application
main = Blueprint('main', __name__)

@main.route('/')
def fetch_csv():
    return render_template_string("<h1>hi there</h1>")
