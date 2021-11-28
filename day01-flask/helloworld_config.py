from flask import Flask


# class DefaultConfig(object):
#     """
#     默认配置
#     """
#     SECRET_KEY = 'chiafjkafjasflajdfaf'


app = Flask(__name__, static_url_path='/s', static_folder='static_files')  # static_url_path 改变名字 static_folder 改变目录

# 设置
# app.config.from_object(DefaultConfig) # 从配置中
# app.config.from_pyfile('setting.py') # 从配置文件中获取
# app.config.from_envvar('PROJECT_SETTING') # 从配置文件中获取
@app.route('/')
def index():
    print(app.config['SECRET_KEY'])
    return 'Hello World'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
