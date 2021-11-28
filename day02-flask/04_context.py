from flask import Flask, request, abort, current_app, g

app = Flask(__name__)


#
# # redis-cli
#
# app.redis_cli = 'redis client'
#
#
# @app.route('/articles')
# def get_articles():
#     channel_id = request.args.get('channel_id')
#     print(app.redic_cli)
#     if channel_id is None:
#         abort(400)
#     return 'you wanna get articles of channel {}'.format(channel_id)
#
#
# from passport import bp
#
# app.register_blueprint(bp)


def db_query():
    user_id = g.user_id
    user_name = g.user_name
    print('user_id={} user_name={}'.format(user_id, user_name))


@app.route('/')
def get_user_profile():
    g.user_id = 123
    g.user_name = 'itcast'
    db_query()
    return 'hello world'

# app1 = Flask(__name__)
# app2 = Flask(__name__)
# # redis-cli
#
# app1.redis_cli = 'redis client 1'
# app2.redis_cli = 'redis client 2'
#
#
# @app1.route('/app1')
# def get_articles_1():
#     return '{}'.format(current_app.redis_cli)
#
#
# @app2.route('/app2')
# def get_articles_2():
#     return '{}'.format(current_app.redis_cli)
