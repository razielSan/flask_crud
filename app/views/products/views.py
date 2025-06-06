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

    if name == "fuck":
        raise Exception("Плохой запрос")

    product_storage.add(name=name, price=price)
    return render_template(
        "products/components/_products-list.html",
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
