from flask import Flask

app = Flask(__name__, template_folder='../../front-end/templates')

from . import routes
