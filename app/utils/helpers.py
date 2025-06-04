from flask import request


def is_backround_request():
    return bool(request.headers.get("Hx-Request"))