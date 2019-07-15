#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:
from flask import Flask,render_template,flash,request,redirect,url_for

from flask_sqlalchemy import  SQLAlchemy
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import  DataRequired

pymysql.install_as_MySQLdb()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@127.0.0.1/flask_books'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key ='abc'
db =SQLAlchemy(app)



#@定义书和作者模型
class Author(db.Model):
    #表名
    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    books = db.relationship('Book',backref='author')

    def __repr__(self):
        return 'Author: %s' %self.name
class Book(db.Model):
    #表名
    __tablename__= 'books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)
    author_id = db.Column(db.Integer,db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book: %s %s' %(self.name,self.author_id)



#自定义_表单类
class AuthorForm(FlaskForm):
    author =StringField('作者',validators=[DataRequired()])
    book = StringField('书籍',validators=[DataRequired()])
    submit = SubmitField('提交')

@app.route('/delete_book/<book_id>')
def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除书籍出错')
            db.session.rollback()
    else:
        flash('书籍找不到')


    return redirect(url_for('index'))




@app.route('/',methods=['GET','POST'])
def index():
    authform =AuthorForm()
    if authform.validate_on_submit():
        author_name = authform.author.data
        book_name = authform.book.data

        author = Author.query.filter_by(name=author_name).first()
        if author:
            book=Book.query.filter_by(name=book_name).first()
            if book:
                flash('已存在同名书籍')
            else:
                try:
                    new_book = Book(name=book_name,author_id=author.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加书籍失败')
                    db.session.rollback()
        else:
            try:
                new_author = Author(name=author_name)
                db.session.add(new_author)
                db.session.commit()

                new_book = Book(name=book_name,author_id=new_author.id)
                db.session.add(new_book)

                db.session.commit()

            except Exception as e:
                print(e)
                flash('添加书籍失败')
                db.session.rollback()
    else:
        if request.method =='POST':
            flash('参数不全！')


    '''
    逻辑验证
    1.通过WTF函数实现验证
    2.验证通过获取数据
    3.判断作者是否存在
    4.如果作者存在，判断书籍是否存在，没有重复数据就添加数据，如果重复就提示错误
    5.如果作者不存在，就添加作者和书籍
    6.验证不通过就提示错误
    '''
    authors = Author.query.all()
    return render_template('book.html',authors = authors,form=authform)



@app.route('/delete_author/<author_id>')
def delete_author(author_id):
    author = Author.query.get(author_id)
    if author:
        try:
            books = Book.query.filter_by(author_id=author_id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    else:
        flash('删除作者出错')
    return  redirect(url_for('index'))
if __name__=='__main__':
    db.drop_all()
    db.create_all()


    #生成数据
    au1= Author(name='老王')
    au2 = Author(name='老李')
    au3 = Author(name='老张')

    db.session.add_all([au1,au2,au3])
    db.session.commit()

    bk1 = Book(name='老王回忆录',author_id = au1.id)
    bk2 = Book(name='我读书少',author_id=au1.id)
    bk3 = Book(name='如何征服少年', author_id=au2.id)
    bk4 = Book(name='天王在少', author_id=au3.id)
    bk5 = Book(name='牛逼归来', author_id=au3.id)
    bk6 = Book(name='未23', author_id=au3.id)

    db.session.add_all([bk1,bk2,bk3,bk4,bk5,bk6])
    db.session.commit()


    app.run(debug=True)





