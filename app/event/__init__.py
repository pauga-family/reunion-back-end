from flask import Blueprint

bp = Blueprint('event', __name__)

from app.event import event_service, event_model, event_routes