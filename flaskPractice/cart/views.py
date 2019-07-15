#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

# coding:utf-8

#view.py  中的。 表示所属的模块
from . import  app_cart
from flask import  render_template


@app_cart.route("/get_cart")
def get_cart():
    return render_template("cart.html")