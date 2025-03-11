from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin

db = SQLAlchemy()

roles_users = Table(
    "roles_users",
    Column("user_id", Integer, ForeignKey('user.id')),
    Column("role_id", Integer, ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False, unique=True)
  users = relationship('User', secondary=roles_users, back_populates='roles')


class User(db.Model, UserMixin):
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)
  active = Column(Boolean, default=True)
  roles = relationship('Role', secondary=roles_users, back_populates='users')
