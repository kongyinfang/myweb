from flask import Blueprint

main = Blueprint('user', __name__)

from . import views
# from .. import errors