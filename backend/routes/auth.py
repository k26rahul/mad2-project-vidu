from flask import Blueprint, request, jsonify
from flask_security.utils import login_user, logout_user, verify_password
from models import db, User

auth_bp = Blueprint('auth_bp', __name__)
bp = auth_bp


@bp.route('/api/login')
def login():
  email = request.form.get('email')
  password = request.form.get('password')
  user = User.query.filter_by(email=email).first()

  if user and verify_password(password, user.password):
    return jsonify({
        "message": 'login successful'
    })

  return jsonify({
      "message": 'email or password incorrect'
  }), 401


@bp.route('/api/logout')
def logout():
  return 'OK'


@bp.route('/api/register/customer')
def register_customer():
  return 'OK'


@bp.route('/api/register/professionals')
def register_professionals():
  return 'OK'
