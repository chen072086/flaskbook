#encoding:utf-8

from flask import  Flask
from database import  config
import  pymysql
from flask_sqlalchemy import  SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
pymysql.install_as_MySQLdb()
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)

#article表：
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('articles'))

db.create_all()

@app.route('/')
def hello_world():
    #增加数据
    # article1 = Article(title='aaa',content='bbb')
    # db.session.add(article1)
    # db.session.commit()

    #查
    #select * from article where acticle.title='aaa'
    # articel1 = Article.query.filter(Article.title =='aaa').first()
    # print ('title :%s' %articel1.title)

    #改，先查出来再进行修改
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # article1.title = 'new title'
    # db.session.commit()

    #删除，先查出来再进行删除
    # article1 =Article.query.filter(Article.title =='new title').first()
    # db.session.delete(article1)
    # db.session.commit()
    # user1 = User(username='zhiliao')
    # db.session.add(user1)
    # db.session.commit()
    #
    #
    # article = Article(title='aaa',content='bbb',author_id=1)
    # db.session.add(article)
    # db.session.commit()
    #我要找文章标题为aaa的这个作者

    article = Article.query.filter(Article.title =='aaa').first()
    print('username:%s' %article.author.username)

    return 'Hello World!'

if __name__=='__main__':
    app.run(debug=True)

