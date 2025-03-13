from flask import Blueprint
from flask_security import roles_required

customer_bp = Blueprint('customer_bp', __name__)
bp = customer_bp


@bp.route('/api/customer/test')
@roles_required('customer')
def test():
  return 'ALL OK'
