#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX
# coding:utf-8

from flask import Flask,request,jsonify


app= Flask(__name__)

@app.route("/login",methods=["POST"])
def login():
    #接受参数
    username = request.form.get("username")
    password = request.form.get("password")

    #参数判断
    if not all([username,password]):
        resq ={
            "code":1,
            "message":"invalid params"
        }
        return jsonify(resq)
    if username =="admin" and password=="python":
        resq = {
            "code": 0,
            "message": "logim success"
        }
        return  jsonify(resq)
    else:
        resq = {
            "code": 2,
            "message": "wrong user name or password"
        }
    return  jsonify(resq)

if __name__ == '__main__':
    app.run(debug=True)




