from flask import request


def is_backround_request():
    hx_request = request.headers.get("Hx-Request")
    boosted = request.headers.get("Hx-Boosted")
    return bool(hx_request) and not boosted

