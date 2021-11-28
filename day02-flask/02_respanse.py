from flask import Flask, render_template, make_response, request, session
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class DefaultConfig(object):
    SECRET_KEY = 'fih9fh9eh9gh2'


app.config.from_object(DefaultConfig)

# 或者直接设置
# app.secret_key = 'xihwidfw9efw'


# @app.route('/users/<user_id>')
# @app.route('/users/<string:user_id>')
# @app.route('/')
# def home():
#     mint = 123
#     mstr = 'itcst'
#     data = dict(
#         my_str=123,
#         my_int = 'itcst'
#     )
#
#
#     # return render_template('index.html', my_str=mstr, my_int=mint)
#     return render_template('index.html', **data)

@app.route('/demo4')
def demo4():
    # return '状态码为 666', 666
    # return '状态码为 666', 666, [('Itcast', 'Python')]
    return '状态码为 666', 666, {'Itcast': 'Python'}


@app.route('/demo5')
def demo5():
    resp = make_response('make response测试')
    resp.headers['Itcast'] = 'Python'
    resp.status = '404 not found'
    return resp


@app.route('/cookie')
def set_cookie():
    resp = make_response('set cookie ok')
    resp.set_cookie('username', 'itcast', max_age=3600)
    return resp


@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp


@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('hello world')
    response.delete_cookie('username')
    return response


@app.route('/set_session')
def set_session():
    session['username'] = 'itcast'
    return 'set session ok'


@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'get session username {}'.format(username)
