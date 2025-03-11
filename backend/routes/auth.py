from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)
bp = auth_bp


@bp.route('/api/login')
def login():
  return 'OK'


@bp.route('/api/register/customer')
def register_customer():
  return 'OK'


@bp.route('/api/register/professionals')
def register_professionals():
  return 'OK'
