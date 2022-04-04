import json

from flask import Blueprint, jsonify, request
from sqlalchemy import and_

from models.users import Users
from models.roles import Roles
from models import db
from utils.string_util import calc_sha1
from utils.jwt_util import generate_jwt


login_bp = Blueprint('login', __name__, url_prefix='/api/v1')


@login_bp.post("/login")
def user_login_view():
    body: dict = request.json
    name: str = body.get("username")
    password: str = body.get("password")
    password = calc_sha1(password)
    user = db.session.query(Users.id, Roles.menus, Users.role_id). \
        join(Roles, Users.role_id == Roles.id). \
        filter(and_(Users.is_deleted == 0, Users.username == name, Users.password == password)).first()
    if user is None:
        return jsonify({"msg": "auth failed", "status": 1})
    menus, user_id = json.loads(user.menus), user.id
    token, exp = generate_jwt({"user_id": user_id, "menus": menus})
    res = jsonify({"data": {"_id": user_id, "username": name, "role_id": user.role_id,
                            "role": {"menus": menus}, 'token': token,
                            'expires': exp}, "status": 0})
    return res

