from flask import Blueprint, jsonify, current_app, request
from sqlalchemy.orm import load_only

from models.users import Users
from models.roles import Roles
from models import db
from utils.string_util import calc_sha1
from utils.time_utils import gen_timestamp


user_bp = Blueprint('user', __name__, url_prefix='/api/v1/manage/user')


@user_bp.get('/list')
def list_user_view():
    user_list = Users.query.options(load_only(
        Users.id, Users.username, Users.email, Users.phone,
        Users.create_time, Users.role_id)).filter_by(is_deleted=0).all()
    users = []
    for user in user_list:
        users.append({
            "_id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "create_time": str(user.create_time),
            "role_id": user.role_id
        })
    # current_app.logger.info(f'users: {users}')
    roles_list = Roles.query.options(load_only(
        Roles.id, Roles.name)).filter_by(is_deleted=0).all()
    roles = []
    for role in roles_list:
        roles.append({
            "_id": role.id,
            "name": role.name
        })
    return jsonify({"data": {"users": users, "roles": roles}, "status": 0})


@user_bp.post("/add")
def add_user_view():
    body: dict = request.json
    username: str = body.get("username")
    password: str = body.get("password")
    password = calc_sha1(password)
    phone: str = body.get("phone")
    email: str = body.get("email")
    role_id: int = body.get("role_id")
    try:
        user = Users(username=username, password=password, phone=phone, email=email, role_id=role_id)
        db.session.add(user)
        db.session.commit()
        return jsonify({"status": 0})
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 0, "msg": "system error"})


@user_bp.post("/update")
def update_user_view():
    body: dict = request.json
    username: str = body.get("username")
    phone: str = body.get("phone")
    email: str = body.get("email")
    role_id: int = body.get("role_id")
    _id: int = body.get("_id")
    try:
        Users.query.filter_by(id=_id).update({'username': username,
                                              'phone': phone, 'email': email,
                                              'role_id': role_id})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@user_bp.post("/delete")
def delete_user_view():
    body: dict = request.json
    _id: int = body.get("userId")
    try:
        Users.query.filter_by(id=_id).update({'is_deleted': gen_timestamp()})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})
