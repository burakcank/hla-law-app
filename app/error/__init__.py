from flask import Blueprint

error_bp = Blueprint("error_bp", __name__, template_folder="templates")

import app.error.views
