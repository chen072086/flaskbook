#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

import  unittest
from author_book import  Author,db,app

class DatabaseTest(unittest.TestCase):
    def setUp(self):

        app.DATABASE = 'flask_test'
        app.testing= True
        db.crate_all()
    def  test_add_author(self):
        """测试添加作者的数据库操作"""
        author = Author(name="zhangsan",email="itcaset@itcast.cn",mobile="18612345678")
        db.session.add(author)
        db.session.commit()
        import  time
        time.sleep(20)
        result_author = Author.query.filter_by(name="zhang").first()
        self.assertIsNotNone(result_author)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
