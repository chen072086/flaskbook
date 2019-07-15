from flask import  Flask,render_template , request
from flask_sqlalchemy import SQLAlchemy
from models import UserMode
from database import  config
from exts import  db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__=='__main__':
    app.run()