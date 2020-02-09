from flask import Blueprint, jsonify, request
from . import db
from .models import Crop

main = Blueprint('main', __name__)


@main.route('/add_crop', methods=['POST'])
def add_crop():
    crop_data = request.get_json()  # crop_data => JSON Obj

    new_crop = Crop(name=crop_data['name'], location=crop_data['location'])

    db.session.add(new_crop)
    db.session.commit()

    return 'Done', 201  # 201 => something wascreated successfully


@main.route('/crops')
def crops():
    crops = []
    return jsonify({'crops': crops})
