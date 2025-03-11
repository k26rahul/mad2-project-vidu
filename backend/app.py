from flask import Flask
from models import db, Role, User
from flask_security import Security, SQLAlchemyUserDatastore
from populate_db import populate

from routes.auth import auth_bp
from routes.admin import admin_bp
from routes.customer import customer_bp
from routes.professionals import professionals_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
app.config['SECURITY_PASSWORD_SALT'] = 'qwerty'

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(professionals_bp)

db.init_app(app)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_blueprint=False)

with app.app_context():
  db.create_all()
  populate()


if __name__ == '__main__':
  app.run(debug=True)
