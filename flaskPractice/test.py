'''
两张表
角色
用户（角色ID）
'''
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    #定义字段
    id = db.Column(db.Integer,primary_kye=True)
    name = db.Column(db.String(16),unique = True)
    #在一的地方，写关联:
    users = db.relationship('User',backref='role')

class User(db.Model):
    __tablename__= 'users'
    id= db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(16),unique= True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))



if __name__=='__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)


