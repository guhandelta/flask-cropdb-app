from flask import Blueprint, jsonify, request
from . import db  # . -> looking in the __init__ file
from .models import Crop

main = Blueprint('main', __name__)


@main.route('/add_crop', methods=['POST'])
def add_crop():
    crop_data = request.get_json()  # crop_data => JSON Obj

    new_crop = Crop(name=crop_data['name'], price=crop_data['price'])

    db.session.add(new_crop)
    db.session.commit()

    return 'Done', 201  # 201 => something wascreated successfully


@main.route('/crops')
def crops():
    crop_list = Crop.query.all()
    crops = []

    for crop in crop_list:
        crops.append({"name": crop.name, "price": crop.price})

    return jsonify({'crops': crops})
