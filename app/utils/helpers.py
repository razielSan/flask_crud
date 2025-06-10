from flask import request
from werkzeug.exceptions import NotFound

from views.products.crud import product_storage


def is_backround_request():
    hx_request = request.headers.get("Hx-Request")
    boosted = request.headers.get("Hx-Boosted")
    return bool(hx_request) and not boosted


def get_product(product_id: int):
    product = product_storage.get_product_by_id(product_id)
    if product:
        return product
    raise NotFound(f"Product with id {product_id} does not exist")
