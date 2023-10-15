from flask import Blueprint

bp = Blueprint('user', __name__)

from app.User import UserModel, UserRoutes, UserService