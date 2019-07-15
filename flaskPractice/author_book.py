#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX
#coding:utf-8
import  pymysql
pymysql.install_as_MySQLdb()

from flask import  Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import  SQLAlchemy
from flask_wtf import  FlaskForm

from wtforms import  StringField,SubmitField
from wtforms.validators import  DataRequired

from flask_migrate import Migrate,MigrateCommand
from flask_script import Shell,Manager


app = Flask(__name__)

manager = Manager(app)


class Config(object):
    DIALECT = 'mysql'
    DRIVER = 'mysqldb'
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'author_book_py4'

    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER,
                                                                           USERNAME, PASSWORD, HOST, PORT, DATABASE)


    #SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/author_book_py4"

    SQLALCHEMY_TRACK_MODIFICATIONS = True

app.config.from_object(Config)

db=SQLAlchemy(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

app.secret_key = "aasdfdsf"
class Author(db.Model):
    __tablename__="tbl_authors"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    books = db.relationship("Book",backref="author")
    email = db.Column(db.String(32),unique=True)
class Book(db.Model):

    __tablename__="tbl_books"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique = True)
    author_id = db.Column(db.Integer,db.ForeignKey("tbl_authors.id"))

class AuthorBookForm(FlaskForm):
    """作者书籍表单类"""
    author_name =StringField(label="作者",validators=[DataRequired("作者必填")])
    book_name=StringField(label="书籍",validators=[DataRequired("书籍必填")])
    submit= SubmitField(label="保存")

@app.route("/",methods = ["GET","POST"])
def index():
    #查询数据库
    form = AuthorBookForm()
    if form.validate_on_submit():
        author_name = form.author_name.data
        book_name = form.author_name.data

        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()
        #book = Book(name=book_name,author_id = author.id)
        book = Book(name=book_name,author=author)
        db.session.add(book)
        db.session.commit()
    authors_li = Author.query.all()
    return  render_template("author_book.html",authors=authors_li,form = form)

#
#
# @app.route("/delete_book",method=["POST"])
# def delete_book():
#     #提取参数
#     req_dict = request.get_json()
#     book_id = req_dict.get("book_id")
#
#     book =Book.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#     return  redirect(url_for("index"))

#/delete_book/book_id
@app.route("/delete_book/<int:book_id>",methods=["GET"])
def delete_book(book_id):
    #提取参数
    req_dict = request.get_json()
    #book_id = request.args.get("book_id")
    print(book_id)
    book =Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return  redirect(url_for("index"))

#/delete_book?book_id=#
# @app.route("/delete_book",methods=["GET"])
# def delete_book():
#     #提取参数
#     book_id = request.args.get("book_id")
#     book =Book.query.get(book_id)
#     db.session.delete(book)
#     db.session.commit()
#     return  redirect(url_for("index"))

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    #
    # au_xi = Author(name = '我爱吃西红柿')
    # au_qian = Author(name = '萧小')
    # au_san = Author(name = '唐家三少')
    # db.session.add_all([au_xi,au_qian,au_san])
    # db.session.commit()
    #
    # bk_xi = Book(name='吞噬星空',author_id=au_xi.id)
    # bk_xi1 = Book(name='寸芒',author_id=au_qian.id)
    # bk_xi2 = Book(name='缥缈之旅',author_id=au_san.id)
    # db.session.add_all([bk_xi, bk_xi1, bk_xi2])
    # db.session.commit()
    #app.run(debug=True)
    manager.run()

