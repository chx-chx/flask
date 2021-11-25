# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask

# app = Flask(__name__) # -> Flask(模块名字符串类型)
# app = Flask(__name__, static_url_path='/s')
app = Flask(__name__, static_url_path='/s', static_folder='static_files')  # static_url_path 改变名字 static_folder 改变目录


@app.route('/',methods=['POST'])
def index():
    return 'Hello World'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
