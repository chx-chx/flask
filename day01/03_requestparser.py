from flask import Flask, Blueprint, request
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser
import re

app = Flask(__name__)
api = Api(app)


def mobile(mobile_str):
    """
    检验手机号格式
    :param mobile_str: str 被检验字符串
    :return: mobile_str
    """
    if re.match(r'^1[3-9]\d{9}$', mobile_str):
        return mobile_str
    else:
        raise ValueError('{} is not a valid mobile'.format(mobile_str))


# /demo?a=1
class DemoResource(Resource):

    def get(self):
        # a = request.args.get('a')
        # if not a:
        #     pass
        # else:
        #     pass
        # 1.创建Requesparser类对象
        rp = RequestParser()

        # 2.声明参数
        # rp.add_argument('a')
        rp.add_argument('a', type=mobile, required=True, action='append')
        # 3.执行检验
        req = rp.parse_args()

        # 可以将req当作字典，也可以当作对象
        # a = req['a']

        # rp.add_argument('a', type=int, required=True, help='missing a param', action='append')

        a = req.a
        return {'a': a}

    def post(self):
        return {'msg': 'post view'}


api.add_resource(DemoResource, '/demo')
