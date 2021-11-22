from flask import Flask


class DefaultConfig(object):
    """
    默认配置
    """
    SECRET_KEY = 'chiafjkafjasflajdfaf'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


def create_flask_app(config):
    """
    创建flask对象的工厂函数
    """
    app = Flask(__name__, static_url_path='/s', static_folder='static_files')  # static_url_path 改变名字 static_folder 改变目录

    # 设置
    app.config.from_object(config)  # 从配置中
    app.config.from_envvar('PROJECT_SETTING')  # 从配置文件中获取
    return app


app = create_flask_app(DevelopmentConfig)

@app.route('/')
def index():
    print(app.config['SECRET_KEY'])
    return 'Hello World'


#
# if __name__ == '__main__':
#     app.run()
#
