from flask import  Blueprint


# 创建蓝图
goods_bp = Blueprint('goods', __name__)
from . import views
