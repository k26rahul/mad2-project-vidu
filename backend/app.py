from flask import Flask
from models import db, Role, User
from flask_security import Security, SQLAlchemyUserDatastore
from populate_db import populate

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.config['SECURITY_PASSWORD_SALT'] = 'qwerty'

db.init_app(app)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_blueprint=False)

with app.app_context():
  db.create_all()
  populate()


@app.route('/')
def index():
  return 'hello from app.py, in wsl'


if __name__ == '__main__':
  app.run(debug=True)
