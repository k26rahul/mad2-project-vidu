from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin
import uuid

db = SQLAlchemy()


class Base(db.Model):
  __abstract__ = True  # very important

  def to_dict(self):
    # https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class UserRoles(Base):
  id = Column(Integer, primary_key=True, autoincrement=True)
  user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
  role_id = Column(Integer, ForeignKey('role.id'), nullable=False)


class Role(Base, RoleMixin):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False, unique=True)

  users = relationship('User', secondary='user_roles', back_populates='roles')


class User(Base, UserMixin):
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)
  active = Column(Boolean, default=True)
  fs_uniquifier = Column(String, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))

  roles = relationship('Role', secondary='user_roles', back_populates='users')
  customer = relationship('Customer', back_populates='user')
  professional = relationship('Professional', back_populates='user')


class Customer(Base):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  location = Column(String, nullable=False)
  pincode = Column(String, nullable=False)
  user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

  user = relationship('User', back_populates='customer')
  service_requests = relationship('ServiceRequest', back_populates='customer')


class Professional(Base):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  location = Column(String, nullable=False)
  pincode = Column(String, nullable=False)
  user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
  service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
  is_approved = Column(Boolean, default=False)

  user = relationship('User', back_populates='professional')
  service = relationship('Service', back_populates='professionals')
  service_requests = relationship('ServiceRequest', back_populates='professional')


class Service(Base):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  price = Column(Float, nullable=False)
  description = Column(String)
  time_required = Column(Integer, default=60)

  professionals = relationship('Professional', back_populates='service')
  service_requests = relationship('ServiceRequest', back_populates='service')


class ServiceRequest(Base):
  id = Column(Integer, primary_key=True, autoincrement=True)
  customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
  professional_id = Column(Integer, ForeignKey('professional.id'), nullable=False)
  service_id = Column(Integer, ForeignKey('service.id'), nullable=False)
  status = Column(String, default='requested')
  service_date = Column(Date, nullable=False)
  rating = Column(Integer)
  remarks = Column(String)

  customer = relationship('Customer', back_populates='service_requests')
  professional = relationship('Professional', back_populates='service_requests')
  service = relationship('Service', back_populates='service_requests')
