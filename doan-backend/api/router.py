from flask import Blueprint, redirect, url_for

from api.handler import (
    auth,
    middleware,
)

bp = Blueprint("default", __name__)

bp.add_url_rule(
    "/login", view_func=auth.login, methods=["POST"], endpoint="login"
)


@bp.before_request
def before_request():
    return middleware.check_auth()