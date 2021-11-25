from flask import Flask
import json

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


# @app.route('/')
# def index():
#     print(app.config['SECRET_KEY'])
#     return 'Hello World'


# print(app.url_map) -> Map对象
# 需求 需要遍历url_map 取出特定信息 在一个特性接口返回
#
# for rule in app.url_map.iter_rules():
#     print('name={} path={}'.format(rule.endpoint, rule.rule))
@app.route('/')
def route_map():
    """
    主视图，返回所有识图网址
    :return:
    """
    rules_iterator = app.url_map.iter_rules()
# {'index':'/','static':'/s/xxx'}
    return json.dumps({rule.endpoint:rule.rule for rule in rules_iterator})

# if __name__ == '__main__':
#     app.route_map()
#
