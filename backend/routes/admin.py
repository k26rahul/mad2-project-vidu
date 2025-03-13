from flask import Blueprint, jsonify
from models import Customer
from flask_security import login_required, auth_required, roles_required, roles_accepted

admin_bp = Blueprint('admin_bp', __name__)
bp = admin_bp


@bp.route('/api/whoami')
# @auth_required()
def whoami():
  from flask_security import current_user
  return jsonify({
      'user': current_user.email if current_user.is_authenticated else None,
      'role': current_user.role.name if current_user.is_authenticated and current_user.role else None
  })


@bp.route('/api/admin/customers')
@auth_required('session')
@roles_accepted('admin')
def customers():
  # get all customers data
  customers = Customer.query.all()
  return jsonify(customers)


# get all professionals data
# block/unblock user (customer/professional both)
# approve/reject professional
# create/edit/delete services
# search professionals [name, location, pincode, service]
# get summary data
