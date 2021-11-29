from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

bp = Blueprint('bp', __name__)

# class HelloWorldResource(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
#     def post(self):
#         return {'msg': 'post hello world'}

api = Api(bp)


class HelloWorldResource(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}


api.add_resource(HelloWorldResource, '/')
# if __name__ == '__main__':
#     app.run(debug=True)

app.register_blueprint(bp)
