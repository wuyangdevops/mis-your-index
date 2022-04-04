from flask import Blueprint, jsonify, current_app, request
from sqlalchemy.orm import load_only
from sqlalchemy import func

from models.products import Products
from models import db

product_bp = Blueprint('product', __name__, url_prefix='/api/v1/manage/product')


@product_bp.post("/add")
def add_product_view():
    body: dict = request.json
    name = body.get('name')
    desc = body.get('desc')
    price = body.get('price')
    p_category_id = body.get('pCategoryId')
    category_id = body.get('categoryId')
    try:
        product = Products(name=name, desc=desc,
                           price=price, parent_category_id=p_category_id,
                           category_id=category_id)
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@product_bp.post("/update")
def update_product_view():
    body: dict = request.json
    name = body.get('name')
    desc = body.get('desc')
    price = body.get('price')
    p_category_id = body.get('pCategoryId')
    category_id = body.get('categoryId')
    _id = body.get("_id")
    try:
        Products.query.filter_by(id=_id).update({'name': name, 'desc': desc,
                                                 'price': price,
                                                 'parent_category_id': p_category_id,
                                                 'category_id': category_id})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@product_bp.post("/updateStatus")
def update_product_status_view():
    body: dict = request.json
    _id = body.get("productId")
    status = int(body.get("status"))
    if status not in (1, 2):
        return jsonify({"status": 1, "msg": "invalid status"})
    try:
        Products.query.filter_by(id=_id).update({'on_sale': status})
        db.session.commit()
    except Exception as e:
        current_app.logger.error(f'database error, {e}')
        db.session.rollback()
        return jsonify({"status": 1, "msg": "system error"})
    else:
        return jsonify({"status": 0})


@product_bp.get("/list")
def list_product_view():
    params = request.args
    page = int(params.get('pageNum', 1))
    size = int(params.get('pageSize', 3))
    count = db.session.query(func.count(Products.id)).filter(Products.is_deleted == 0).scalar()
    current_app.logger.info(f'count is {count}')
    product_list = Products.query.options(load_only(
        Products.id, Products.name, Products.desc,
        Products.price, Products.on_sale)).filter_by(is_deleted=0).limit(size).offset((page - 1) * size).all()
    products = []
    for product in product_list:
        products.append({'_id': product.id, 'name': product.name,
                         'desc': product.desc, 'price': product.price, 'status': product.on_sale})
    return jsonify({"data": {"total": count, "list": products}, "status": 0})


@product_bp.get("/search")
def search_product_view():
    params = request.args
    page = int(params.get('pageNum', 1))
    size = int(params.get('pageSize', 3))
    product_name = params.get('productName')
    product_desc = params.get('productDesc')
    if product_name is None and product_desc is None:
        return jsonify({'status': 1, 'msg': 'invalid search condition'})
    if product_name:
        count = db.session.query(func.count(Products.id)).filter(Products.is_deleted == 0,
                                                                 Products.name.like(f'%{product_name}%')).scalar()
        current_app.logger.info(f'count is {count}')
        product_list = Products.query.options(load_only(
            Products.id, Products.name, Products.desc,
            Products.price, Products.on_sale)).filter(Products.is_deleted == 0,
                                                      Products.name.like(f'%{product_name}%')).limit(size).offset(
            (page - 1) * size).all()
    else:
        count = db.session.query(func.count(Products.id)).filter(Products.is_deleted == 0,
                                                                 Products.desc.like(f'%{product_desc}%')).scalar()
        current_app.logger.info(f'count is {count}')
        product_list = Products.query.options(load_only(
            Products.id, Products.name, Products.desc,
            Products.price, Products.on_sale)).filter(Products.is_deleted == 0,
                                                      Products.desc.like(f'%{product_desc}%')).limit(size).offset(
            (page - 1) * size).all()
    products = []
    for product in product_list:
        products.append({'_id': product.id, 'name': product.name,
                         'desc': product.desc, 'price': product.price, 'status': product.on_sale})
    return jsonify({"data": {"total": count, "list": products}, "status": 0})
