from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


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
    print(type(mob_num))
    return 'send sms code to {}'.format(mob_num)
