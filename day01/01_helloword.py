from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorldResource(Resource):
    def get(self):
        return {'hello': 'world'}

        def post(self):
        return {'msg': 'post hello world'}

api.add_resource(HelloWorldResource, '/')
