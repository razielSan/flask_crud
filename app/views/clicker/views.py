from flask import Blueprint, render_template, request

from templates.clicker.crud import Clicker


router = Blueprint("clicker", __name__)

clicker = Clicker()


@router.route("/", methods=["POST", "GET"], endpoint="click")
def show_clicker_page():
    if request.method == "POST":
        clicker.inc_count()
        return render_template("clicker/clicker.html", count=clicker.count)
    return render_template("clicker/clicker.html", count=0)
