from flask import Blueprint, render_template, request

from templates.clicker.crud import Clicker
from utils.helpers import is_backround_request


router = Blueprint("clicker", __name__)

clicker = Clicker()


@router.route("/", methods=["POST", "GET"], endpoint="click")
def show_clicker_page():
    if request.method == "POST":
        template_name = "clicker/clicker.html"
        if is_backround_request():
            clicker.inc_count()
            template_name = "clicker/components/_clicker-count.html"
        else:
            clicker.inc_count_form()
        return render_template(
            template_name,
            count=clicker.count,
            form_count=clicker.count_form,
        )

    template_name = "clicker/clicker.html"
    if is_backround_request():
        template_name = "clicker/components/_clicker-body.html"
    return render_template(
        template_name,
        count=clicker.count,
        form_count=clicker.count_form,
    )
