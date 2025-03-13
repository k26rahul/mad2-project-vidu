from models import db, Role, User, Customer, Professional, Service, ServiceRequest
from flask_security import hash_password
from sample_data import services, customers, professionals, service_requests


def populate():
  if not Role.query.first():
    # add roles
    admin_role = Role(name='admin')
    customer_role = Role(name='customer')
    professional_role = Role(name='professional')
    db.session.add_all([admin_role, customer_role, professional_role])

    # add admin
    db.session.add(User(
        email='admin@example.com',
        password=hash_password('12345'),
        role=admin_role
    ))

    # add services
    for service in services:
      db.session.add(Service(**service))

    # add customers
    for customer in customers:
      user = User(
          email=customer['email'],
          password=hash_password('12345'),
          role=customer_role
      )
      customer = Customer(
          name=customer['name'],
          location=customer['location'],
          pincode=customer['pincode'],
          user=user
      )
      db.session.add_all([user, customer])

    # add professionals
    for professional in professionals:
      user = User(
          email=professional['email'],
          password=hash_password('12345'),
          role=professional_role
      )
      professional = Professional(
          name=professional['name'],
          location=professional['location'],
          pincode=professional['pincode'],
          service_id=professional['service_id'],
          user=user
      )
      db.session.add_all([user, professional])

    # add service requests
    for request in service_requests:
      db.session.add(ServiceRequest(**request))

    db.session.commit()
