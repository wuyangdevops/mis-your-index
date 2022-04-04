from flask import Blueprint, jsonify, current_app, request
from sqlalchemy.orm import load_only

from models.categories import Categories
from models import db


category_bp = Blueprint('category', __name__, url_prefix='/api/v1/manage/category')


@category_bp.post("/add")
def add_category_view():
    body: dict = request.json
    category_name: str = body.get('categoryName', '')
    parent_id: int = int(body.get('parentId', 0))
    try:
        category = Categories(name=category_name, parent_id=parent_id)
        db.session.add(category)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@category_bp.post("/update")
def update_category_view():
    body: dict = request.json
    category_id: int = int(body.get('categoryId'))
    category_name: str = body.get('categoryName')
    try:
        Categories.query.filter_by(id=category_id).update({'name': category_name})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@category_bp.get("/list")
def list_category_view():
    params = request.args
    parent_id: int = int(params.get("parentId", 0))
    category_list = Categories.query.options(load_only(
        Categories.id, Categories.name)).filter_by(is_deleted=0, parent_id=parent_id).all()
    categories = []
    for category in category_list:
        categories.append({
            "_id": category.id,
            "name": category.name
        })
    return jsonify({"status": 0, "data": categories})
