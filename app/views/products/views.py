from flask import Blueprint, request, render_template, redirect, url_for, make_response

from views.products.crud import product_storage
from werkzeug.exceptions import BadRequest, HTTPException
from views.products.forms import ProductForm

router = Blueprint("products", __name__)


@router.get("/")
def get_product_list():
    form = ProductForm()

    return render_template(
        "products/list.html",
        list_products=product_storage.get_list,
        form=form,
    )


@router.post("/")
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = product_storage.add(
            name=form.name.data,
            price=form.price.data,
        )
        return render_template(
            "products/components/_form-and-item-oob.html",
            product=product,
            list_products=product_storage.get_list,
            form=ProductForm(formdata=None)
        )
    else:
        render = render_template(
            "products/components/_form.html",
            form=form,
        )
        return make_response(render, 422)


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
