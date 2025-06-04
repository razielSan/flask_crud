from flask import Blueprint, render_template, request

from templates.clicker.crud import Clicker
from utils.helpers import is_backround_request


router = Blueprint("clicker", __name__)

clicker = Clicker()


@router.route("/", methods=["POST", "GET"], endpoint="click")
def show_clicker_page():
    if request.method == "POST":
        if is_backround_request():
            clicker.inc_count()
            return render_template(
                "clicker/components/_clicker-count.html",
                count=clicker.count,
                form_count=clicker.count_form,
            )
        else:
            clicker.inc_count_form()
            return render_template(
                "clicker/clicker.html",
                count=clicker.count,
                form_count=clicker.count_form,
            )
    return render_template(
        "clicker/clicker.html",
        count=clicker.count,
        form_count=clicker.count_form,
    )
