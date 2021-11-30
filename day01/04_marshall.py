from flask import Flask, Blueprint, request
from flask_restful import Resource, Api, fields, marshal_with, marshal
from flask_restful.reqparse import RequestParser
import re

app = Flask(__name__)
api = Api(app)


class User(object):
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age


# 声明需要序列化处理的字段
resoure_fields = {
    'user_id': fields.Integer,
    'name': fields.String
}


class Demo1Resource(Resource):
    @marshal_with(resoure_fields, envelope='data1') # 将数据放入data1中
    def get(self):
        user = User(1, 'itcast', 12)
        return user


class Demo2Resource(Resource):
    def get(self):
        user = User(1, 'itcast', 12)
        return marshal(user, resoure_fields, envelope='data2')


api.add_resource(Demo1Resource, '/demo1')
