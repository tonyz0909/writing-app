from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/results')
def index():
    return render_template('index.html', title='Home')
def results():
    # return 'results'
    return render_template('results.html', title='Results')
