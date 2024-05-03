from flask import Blueprint

bp = Blueprint('user', __name__)

from app.user import user_service, user_model, user_routes