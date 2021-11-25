from flask import Flask, Blueprint

app = Flask(__name__, static_url_path='/s', static_folder='static_files')  # static_url_path 改变名字 static_folder 改变目录

# 创建蓝图
user_bp = Blueprint('user', __name__)


@user_bp.route('/profile')
def get_profile():
    return 'user profile'


# 注册蓝图
app.register_blueprint(user_bp)
app.register_blueprint(user_bp, url_prefix='/user')

from goods import goods_bp

app.register_blueprint(goods_bp)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
