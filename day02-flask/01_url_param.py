from flask import Flask, request, abort
from werkzeug.routing import BaseConverter

app = Flask(__name__)

app.config['itcast']='python'
@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    print(e)
    return '除数不能为0'
# @app.route('/users/<user_id>')
# @app.route('/users/<string:user_id>')
@app.route('/users/<int:user_id>')
def get_users_data(user_id):
    print(type(user_id))
    return 'get_users {}'.format(user_id)


class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


app.url_map.converters['mobile'] = MobileConverter


@app.route('/sms_codes/<mobile:mob_num>')
def send_sms_code(mob_num):
    1/0
    print(type(mob_num))
    return 'send sms code to {}'.format(mob_num)


# /articles?channel_id=123
@app.route('/articles')
def get_articles():
    channel_id = request.args.get('channel_id')
    if channel_id is None:
        abort(400)
    return 'you wanna get articles of channel {}'.format(channel_id)


# 上传图片
@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['pic']
    # with open('./demo.png', 'wb') as new_file:
    #     new_file.write(f.read())
    f.save('./demo.png')
    return 'ok'
