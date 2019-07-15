#encoding:utf-8
from exts import db
from datetime import datetime

class UserMode(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    phone = db.Column(db.String(11),nullable=False)
    password = db.Column(db.String(20),nullable=False)

class Projectlist(db.Model):
    __tablename__='projectlist'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    projectname = db.Column(db.String(20),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)