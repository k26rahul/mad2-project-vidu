from flask import Blueprint, request, jsonify
from flask_security.utils import login_user, logout_user, verify_password
from models import db, User

auth_bp = Blueprint('auth_bp', __name__)
bp = auth_bp


@bp.route('/api/login', methods=['POST'])
def login():
  data = request.get_json()
  email = data.get('email')
  password = data.get('password')
  user = User.query.filter_by(email=email).first()

  if user and verify_password(password, user.password):
    login_user(user)
    return jsonify({
        "success": True,
        "message": 'login successful',
        "role": user.roles[0].name
    })

  return jsonify({
      "success": False,
      "message": 'email or password incorrect'
  }), 401


@bp.route('/api/logout')
def logout():
  logout_user()
  return jsonify({
      'success': True,
      'message': 'logged out successfully'
  })


@bp.route('/api/register/customer')
def register_customer():
  return 'OK'


@bp.route('/api/register/professionals')
def register_professionals():
  return 'OK'
