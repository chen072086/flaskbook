from flask import  Flask,render_template,request,url_for,redirect,session,flash
from flask_script import  Manager
from database import config

from flask_migrate import Migrate,MigrateCommand
from models import  UserMode,Projectlist
import  pymysql

from exts import db
app = Flask(__name__)
app.config.from_object(config)
app.secret_key = 'item'
pymysql.install_as_MySQLdb()
db.init_app(app)



@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.route("/project",methods=['GET','POST'])
def project():
    if request.method =='GET':
        content = {
            'pjcontent':Projectlist.query.all()
        }
        return render_template("project.html", **content)
    else:
        return  redirect(url_for('projectadd'))



@app.route("/projectadd",methods=['GET','POST'])
def projectadd():
    if request.method =='GET':
        return  render_template('projectAdd.html')
    else:
        projectname = request.form.get('projectname')
        pj = Projectlist(projectname=projectname)
        db.session.add(pj)
        db.session.commit()
        return redirect(url_for('project'))

@app.route("/delete")
def deleteproject():
    return u'数据需要删除掉'

@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method =='GET':
        return render_template("login.html")
    else:
        phone = request.form.get('phone')
        password = request.form.get('password')
        user = UserMode.query.filter(UserMode.phone ==phone,UserMode.password ==password).first()
        if user:
            session['user_id'] = user.id
            session.permanent =True
            return redirect(url_for('index'))
        else:
           flash(u'手机号或者密码错误，请确认后再登录！')
           return render_template("login.html")


@app.route("/regist",methods=['GET', 'POST'])
def regist():
    if request.method =='GET':
        return render_template('registration.html')
    else:
        phone =request.form.get('phone')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = UserMode.query.filter(UserMode.phone ==phone).first()
        if user:
            flash(u'号码已注册，请直接登录！')
        else:
            if len(phone) >11:
                flash(u'请输入正确的手机号码')

            if password1 != password2:
                flash(u'两次密码不相等，请核对后再次填写！')
            else:
                user = UserMode(phone=phone,password=password1)
                db.session.add(user)
                db.session.commit()
                return  redirect(url_for('login'))
        return  render_template('registration.html')


@app.route("/testcase",methods=['GET', 'POST'])
def test_suite():
    return  render_template('testsuit.html')

@app.route('/add_test_suite', methods=['POST', 'GET'])
def add_test_suite():
    return render_template("add_testcase.html")





if __name__=='__main__':
    app.run(debug=True)