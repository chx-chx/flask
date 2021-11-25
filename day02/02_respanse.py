from flask import Flask, render_template
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# @app.route('/users/<user_id>')
# @app.route('/users/<string:user_id>')
@app.route('/')
def home():
    mint = 123
    mstr = 'itcst'
    data = dict(
        my_str=123,
        my_int = 'itcst'
    )


    # return render_template('index.html', my_str=mstr, my_int=mint)
    return render_template('index.html', **data)
