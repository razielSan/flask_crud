from flask import Blueprint, render_template


router = Blueprint("index", __name__)


@router.route("/", endpoint="index")
def index_view():
    return render_template("index.html")
