from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.hoas import get_hoas, add_hoa, get_hoa_by_id
import json

hoa_views = Blueprint("hoa", __name__)


@hoa_views.route('/hoas', methods=['GET'])
def get_hoas_view():
    hoas = get_hoas()
    r = []
    for hoa in hoas:
        r.append(hoa.__dict__)
    return make_response(jsonify({"hoas": r}), 200)


@hoa_views.route('/hoa/<hoa_id>', methods=['GET'])
def get_user_by_id_view(hoa_id):
    hoa = get_hoa_by_id(hoa_id)
    result = hoa.__dict__
    return make_response(jsonify({"hoa": result}), 200)


@hoa_views.route('/hoa', methods=['POST'])
def add_hoa_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "name" and "address" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    hoa_name = data["name"]
    hoa_address = data["address"]

    add_hoa(hoa_name, hoa_address)
    return make_response(jsonify({"status": "success"}), 200)
