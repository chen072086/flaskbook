#encoding:utf-8
#
# from flask_script import Manager
# from flask_script_demo import  app
# from db_scripts import  DBManager
# manager = Manager(app)
# @manager.command
# def runserver():
#     print('服务器跑起来了')
#
# manager.add_command('db',DBManager)
#
# if __name__=='__main__':
#     manager.run()

from flask_script import Manager
from migrate_demo import  app
from flask_migrate import Migrate,MigrateCommand
from exts import db
from models import  UserMode

#模型--迁移文件-->表

manager =Manager(app)

migrate = Migrate(app,db)

manager.add_command('db',MigrateCommand)


if __name__=='__main__':
    manager.run()

