from flask import Blueprint, request, render_template

from views.products.crud import product_storage

router = Blueprint("products", __name__)


@router.get("/")
def get_product_list():


    return render_template(
        "products/list.html",
        list_products=product_storage.get_list,
    )
