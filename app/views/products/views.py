from flask import Blueprint, request, render_template, redirect, url_for

from views.products.crud import product_storage

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
    product_storage.add(name=name, price=price)
    return redirect(url_for("products.get_product_list"))
