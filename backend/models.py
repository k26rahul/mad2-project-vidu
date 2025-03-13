from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_security import RoleMixin, UserMixin
import uuid

db = SQLAlchemy()


class Role(db.Model, RoleMixin):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False, unique=True)
  user = relationship('User', back_populates='role')


class User(db.Model, UserMixin):
  id = Column(Integer, primary_key=True, autoincrement=True)
  email = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)
  active = Column(Boolean, default=True)
  fs_uniquifier = Column(String, unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
  role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
  role = relationship('Role', back_populates='user')
  customer = relationship('Customer', back_populates='user')
  professional = relationship('Professional', back_populates='user')


class Customer(db.Model):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  location = Column(String, nullable=False)
  pincode = Column(String, nullable=False)
  user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
  user = relationship('User', back_populates='customer')
  service_requests = relationship('ServiceRequest', back_populates='customer')

  serialize_rules = ('-user.customer', '-user.roles', '-service_requests')


class Professional(db.Model):
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


class Service(db.Model):
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  price = Column(Float, nullable=False)
  description = Column(String)
  time_required = Column(Integer, default=60)
  professionals = relationship('Professional', back_populates='service')
  service_requests = relationship('ServiceRequest', back_populates='service')


class ServiceRequest(db.Model):
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
