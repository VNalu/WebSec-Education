from flask import Blueprint
import sys # For debug print

viewsBP = Blueprint('views', __name__)

from . import views, events
print("init is run!!", views, file=sys.stderr)