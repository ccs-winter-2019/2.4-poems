import csv

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


all_poems = [
    {'title': 'The Variable', 'body': 'Some say....'},
    {'title': 'The List', 'body': 'Some say....'},
    {'title': 'The Tuple', 'body': 'Some say....'},
    {'title': 'Dictionaries', 'body': 'Some say....'},
]

@app.route("/")
def index():

    context = {
        'poems': all_poems,
        'my_name': 'Dan',
        'favorite_flavor': 'coffee',
    }

    return render_template('index.html', **context)


@app.route('/poem/<poem_id>/')
def book_now(poem_id):
    poem_id = int(poem_id)
    poem_index = poem_id - 1

    poem = all_poems[poem_index]

    return render_template('poem_detail.html', poem=poem)
