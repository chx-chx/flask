from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorldResource(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'msg': 'post hello world'}


def decorator1(func):
    def wrapper(*args, **kwargs):
        print('decorator1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    def wrapper(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)

    return wrapper


class DemoResource(Resource):
    method_decorators = [decorator1, decorator2]

    def get(self):
        return {'msg': 'get view'}

    def post(self):
        return {'msg': 'post view'}
