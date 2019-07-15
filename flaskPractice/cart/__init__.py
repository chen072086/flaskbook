# coding:utf-8

from flask import  Blueprint


# 如果有静态目录的话，可以加这个目录static_folder=
#创建了一个蓝图
app_cart = Blueprint("app_cart", __name__,template_folder="templates" )


from .views import get_cart