from models import db, Role, User
from flask_security import hash_password


def populate():
  if not Role.query.first():
    db.session.add(Role(name='admin'))
    db.session.add(Role(name='customer'))
    db.session.add(Role(name='professionals'))
    db.session.commit()

  if not User.query.first():
    admin_role = Role.query.filter_by(name='admin').first()
    customer_role = Role.query.filter_by(name='customer').first()
    professionals_role = Role.query.filter_by(name='professionals').first()

    db.session.add(User(
        email='admin@example.com',
        password=hash_password('12345'),
        roles=[admin_role]
    ))

    db.session.add(User(
        email='customer1@example.com',
        password=hash_password('12345'),
        roles=[customer_role]
    ))

    db.session.add(User(
        email='professionals1@example.com',
        password=hash_password('12345'),
        roles=[professionals_role]
    ))

    db.session.commit()
