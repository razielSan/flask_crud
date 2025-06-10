from flask_wtf import FlaskForm
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, ValidationError
from flask import request

from views.products.crud import product_storage


def validate_product_name(form, field):
    product_name = field.data
    if request.method == "POST" and product_storage.get_check_name_is_exists(
        product_name
    ):
        raise ValidationError(
            f"Product with {product_name!r} already exists!",
        )


class ProductForm(FlaskForm):
    name = StringField(
        label="product name",
        validators=[
            DataRequired(),
            validate_product_name,
        ],
    )
    price = IntegerField(
        label="product price",
        validators=[DataRequired(), NumberRange(max=999_999, min=1)],
    )

    sumbit = SubmitField(label="Add product")
    update_submit = SubmitField(label="Update product")
