from flask import Blueprint, render_template, request, redirect

from csrf_protection import csrf_protect


router = Blueprint("examples", __name__)


@router.route("/", endpoint="examples")
def examples_list():
    return render_template("examples/examples.html")


@csrf_protect.exempt
@router.route("/ping", endpoint="ping", methods=["POST", "GEt"])
def handle_ping():
    if request.method == "POST":
        return "Pong!"
    return render_template("examples/ping/show_ping.html")


@csrf_protect.exempt
@router.route("/hover", methods=["POST", "GET"], endpoint="hover")
def handle_hover():
    if request.method == "POST":
        return "I see you!"
    return render_template("examples/hover/show_hover.html")
