from flask import  Flask
from database import  config
from exts import  db
from models import UserMode
import  pymysql

app = Flask(__name__)
app.config.from_object(config)
pymysql.install_as_MySQLdb()
db.init_app(app)

# with app.app_context():
#     db.create_all()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__=='__main__':
    app.run()