import json

from flask import Blueprint, jsonify, current_app, request
from sqlalchemy.orm import load_only

from models.roles import Roles
from models import db


role_bp = Blueprint('role', __name__, url_prefix='/api/v1/manage/role')


@role_bp.post("/add")
def add_user_view():
    body: dict = request.json
    role_name: str = body.get("roleName")
    try:
        role = Roles(name=role_name)
        db.session.add(role)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@role_bp.post("/update")
def update_role_view():
    body: dict = request.json
    _id: int = body.get("_id")
    auth_name: str = body.get("auth_name")
    menus: list = body.get("menus")
    menus_str: str = json.dumps(menus)
    try:
        Roles.query.filter_by(id=_id).update({'menus': menus_str, 'auth_name': auth_name})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@role_bp.get("/list")
def list_role_view():
    role_list = Roles.query.options(load_only(
        Roles.id, Roles.name, Roles.auth_time, Roles.auth_name,
        Roles.create_time)).filter_by(is_deleted=0).all()
    roles = []
    for role in role_list:
        current_app.logger.info(f'role name: {role.name}')
        roles.append({
            "_id": role.id,
            "name": role.name,
            "create_time": str(role.create_time),
            "auth_time": str(role.auth_time),
            "auth_name": role.auth_name
        })
    return jsonify({"data": roles, "status": 0})
