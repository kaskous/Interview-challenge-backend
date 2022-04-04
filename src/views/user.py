from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.user import get_users, add_user, get_user_by_id
import json

user_views = Blueprint("user", __name__)


@user_views.route('/users', methods=['GET'])
def get_users_view():
    users = get_users()
    r = []
    for user in users:
        r.append(user.__dict__)
    return make_response(jsonify({"users": r}), 200)


@user_views.route('/user/<user_id>', methods=['GET'])
def get_user_by_id_view(user_id):
    user = get_user_by_id(user_id)
    result = user.__dict__
    return make_response(jsonify({"user": result}), 200)


@user_views.route('/user', methods=['POST'])
def add_user_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if "username" not in data:
        return make_response(jsonify({"status": "bad request"}), 400)

    user_name = data["username"]

    add_user(user_name)
    return make_response(jsonify({"status": "success"}), 200)




