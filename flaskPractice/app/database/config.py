import  os
DEBUG = True
SECRET_KEY = os.urandom(24)


DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'mysql'
PASSWORD = 'P@ssword1'
HOST = '10.18.32.132'
PORT = '3306'
DATABASE = 'tsmk_service'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,
                                                                      USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS =True