from time import sleep
from dataclasses import asdict
from http import HTTPStatus

from flask import (
    Blueprint,
    Response,
    request,
    render_template,
    redirect,
    url_for,
    make_response,
)
from werkzeug.exceptions import BadRequest, HTTPException, NotFound

HTTPStatus

from views.products.crud import product_storage
from views.products.forms import ProductForm
from utils.helpers import get_product

router = Blueprint("products", __name__)

PAGE_DEFAULT = 1
PER_PAGE_DEFAULT = 10


@router.get("/")
def get_product_list():
    form = ProductForm()

    all_products = product_storage.get_list
    page = request.args.get("page", PAGE_DEFAULT, type=int)
    per_page = request.args.get("per_page", PER_PAGE_DEFAULT, type=int)
    to_idx = page * per_page
    from_idx = to_idx - per_page
    products = all_products[from_idx:to_idx]

    next_page = to_idx < len(all_products) and page + 1

    template_name = "products/list.html"
    if request.args.get("only_items"):
        template_name = "products/components/_only-items-reveal.html"

    return render_template(
        template_name,
        list_products=products,
        form=form,
        next_page=next_page,
        per_page=per_page,
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
            form=ProductForm(formdata=None),
        )
    else:
        render = render_template(
            "products/components/_form.html",
            form=form,
        )
        return make_response(render, 422)


@router.get("/<int:product_id>")
def get_product_detail(product_id):
    product = get_product(product_id)
    form = ProductForm(data=asdict(product))
    return render_template(
        "products/product-detail.html",
        product=product,
        form=form,
    )


@router.put("/<int:product_id>")
def update_product(product_id):
    print("Hello")
    product = get_product(product_id)
    form = ProductForm(request.form)
    if not form.validate_on_submit():
        response = Response(
            render_template(
                "products/components/_form-update.html",
                form=form,
                product=product,
            ),
            status=HTTPStatus.UNPROCESSABLE_ENTITY,
        )
        raise HTTPException(response=response)
    product_storage.update_product_by_id(
        id=product_id,
        name=form.name.data,
        price=form.price.data,
    )
    return render_template(
        "products/components/_form-update.html",
        form=form,
        product=product,
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


@router.delete("/<int:id>")
def delete_product(id: int):
    # d ={}
    # for i in range(100000):
    #     d[i] = i * i
    sleep(1)
    product_storage.delete_product_by_id(id)
    if request.args.get("redirect"):
        return redirect(url_for("products.get_product_list"), code=HTTPStatus.SEE_OTHER)
    return Response(status=HTTPStatus.NO_CONTENT)
