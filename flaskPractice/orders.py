#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

#coding:utf-8


from flask import Blueprint


app_orders = Blueprint("app_orders",__name__)

@app_orders.route("/get_orders")
def get_orders():
    return 'get_orders page'
