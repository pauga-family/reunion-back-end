from flask import Blueprint

bp = Blueprint('event', __name__)

from app.user import event_model, event_routes, event_service