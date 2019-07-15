#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

#coding:utf-8

from flask import  Flask
from goods import  get_goods
from users import  register
#循环引用，解决方法，推迟一方
from orders import  app_orders

from cart import app_cart

app = Flask(__name__)

app.route("/get_goods")(get_goods)
app.route("/register")(register)

app.register_blueprint(app_orders,url_prefix="/orders")
app.register_blueprint(app_cart,url_prefix="/cart")

@app.route("/")
def index():
    return "index page"

if __name__=="__main__":
    print(app.url_map)
    app.run()


