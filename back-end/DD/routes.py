from . import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pages')
def pages():
    return render_template('pages.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/tiles')
def tiles():
    return render_template('tiles.html')
