from app.error import error_bp
from flask import render_template


@error_bp.app_errorhandler(400)
def page_400(e):
    return render_template("400.html"), 400


@error_bp.app_errorhandler(404)
def page_404(e):
    return render_template("404.html"), 404


@error_bp.app_errorhandler(500)
def page_500(e):
    return render_template("500.html"), 500
