#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX


# coding:utf-8

import  unittest
from login import  app
import  json

class LoginTest(unittest.TestCase):

    def setUp(self):
        """ 在进行测试之前，先被执行"""
        # 创建进行web请求的客户端，使用flask 提供的
        app.config["TESTING"] = True
        app.testing = True
        self.client = app.test_client()

    """构造单元测试案例"""
    def test_empty_user_name_password(self):
        #测试用户名和密码不完整的情况
        #利用client客户端模拟发送web请求
        ret = self.client.post("/login",data={})
        #ret是视图返回的响应对象，data属性是响应体的数据
        resq = ret.data
        #因为login试图返回的是json字符串
        resq = json.loads(resq)

        #拿到返回值后进行断言测试
        self.assertIn("code",resq)
        self.assertEqual(resq["code"],1)

        # 利用client客户端模拟发送web请求
        ret = self.client.post("/login", data={"passwprd":"123456"})
        # ret是视图返回的响应对象，data属性是响应体的数据
        resq = ret.data
        # 因为login试图返回的是json字符串
        resq = json.loads(resq)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resq)
        self.assertEqual(resq["code"], 1)

        # 利用client客户端模拟发送web请求
        ret = self.client.post("/login", data={"username":"adminss"})
        # ret是视图返回的响应对象，data属性是响应体的数据
        resq = ret.data
        # 因为login试图返回的是json字符串
        resq = json.loads(resq)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resq)
        self.assertEqual(resq["code"], 1)

    def test_wrong_user_name_password(self):
        ret = self.client.post("/login", data={"username": "adminss","password":"1214325"})
        # ret是视图返回的响应对象，data属性是响应体的数据
        resq = ret.data
        # 因为login试图返回的是json字符串
        resq = json.loads(resq)

        # 拿到返回值后进行断言测试
        self.assertIn("code", resq)
        self.assertEqual(resq["code"], 2)




if  __name__=='__main__':
    unittest.main()













