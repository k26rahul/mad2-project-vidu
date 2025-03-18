from flask import Blueprint, jsonify
from models import db, Customer, User
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
      "email": c.user.email,
      "active": c.user.active
  } for c in customers]
  return jsonify(data)


@bp.route('/api/admin/block/<int:user_id>')
@roles_required('admin')
def block(user_id):
  # block user (customer/professional both)
  user = User.query.get(user_id)
  user.active = False
  db.session.commit()
  return jsonify({
      "success": True,
      "message": "Blocked successfully"
  })


@bp.route('/api/admin/unblock/<int:user_id>')
@roles_required('admin')
def unblock(user_id):
  # unblock user (customer/professional both)
  user = User.query.get(user_id)
  user.active = True
  db.session.commit()
  return jsonify({
      "success": True,
      "message": "Unblocked successfully"
  })

# get all professionals data
# approve/reject professional
# create/edit/delete services
# search professionals [name, location, pincode, service]
# get summary data
