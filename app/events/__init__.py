from flask import Blueprint

bp = Blueprint('events', __name__)

from app.events import events_service, events_model, events_routes