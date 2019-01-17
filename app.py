import csv

from flask import Flask
from flask import request
from flask import render_template

from poems import all_poems


app = Flask(__name__)


@app.route("/")
def index():

    context = {
        'poems': all_poems,
        'favorite_flavor': 'coffee',
    }

    # return render_template('index.html', poems=all_poems, favorite_flavor='coffee')
    return render_template('index.html', **context)

@app.route('/poem/<poem_id>/')
def book_now(poem_id):
    poem_id = int(poem_id)
    poem_index = poem_id - 1

    poem = all_poems[poem_index]

    ctx = {
        'poem': poem,
    }

    return render_template('poem_detail.html', **ctx)


def register_custom_template_filters():
    import linebreaks

register_custom_template_filters()
