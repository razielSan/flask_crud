from flask import Blueprint, request, render_template, redirect, url_for, make_response

from views.products.crud import product_storage
from werkzeug.exceptions import BadRequest, HTTPException

router = Blueprint("products", __name__)


@router.get("/")
def get_product_list():
    return render_template(
        "products/list.html",
        list_products=product_storage.get_list,
    )


@router.post("/")
def create_product():
    price = request.form.get("price")
    name = request.form.get("name")
    if not price.isdigit():
        render = render_template(
            "products/components/_form.html",
            error="product price should be integer",
        )
        return make_response(render, 422)

    if name == "fuck":
        raise BadRequest("Плохой запрос")

    product = product_storage.add(name=name, price=price)
    return render_template(
        "products/components/_form-and-item-oob.html",
        product=product,
        list_products=product_storage.get_list,
    )


@router.get("/form")
def get_product_list_form():
    return render_template(
        "products/list_form.html",
        list_products=product_storage.get_list,
    )


@router.post("/form")
def create_product_form():
    price = request.form.get("price")
    name = request.form.get("name")
    product_storage.add(name=name, price=price)
    return redirect(url_for("products.get_product_list_form"))
