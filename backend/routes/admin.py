from flask import Blueprint, jsonify
from models import Customer
from flask_security import roles_required
from utils import better_jsonify

admin_bp = Blueprint('admin_bp', __name__)
bp = admin_bp


@bp.route('/api/whoami')
def whoami():
  from flask_security import current_user
  is_authenticated = current_user.is_authenticated
  return jsonify({
      'is_authenticated': is_authenticated,
      'user': current_user.email if is_authenticated else None,
      'role': current_user.roles[0].name if is_authenticated else None
  })


@bp.route('/api/admin/customers')
@roles_required('admin')
def customers():
  # get all customers data
  customers = Customer.query.all()
  data = [{
      **c.to_dict(),
      'email': c.user.email,
      'active': c.user.active
  } for c in customers]
  return jsonify(data)


# get all professionals data
# block/unblock user (customer/professional both)
# approve/reject professional
# create/edit/delete services
# search professionals [name, location, pincode, service]
# get summary data
