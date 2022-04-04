from flask import Blueprint, jsonify, current_app, request
from sqlalchemy import func

from models.products import Products
from models import db


overview_bp = Blueprint('overview', __name__, url_prefix='/api/v1/overview')


@overview_bp.get("/data")
def list_overview_data():
    count = db.session.query(func.count(Products.id)).filter(Products.is_deleted == 0).scalar()
    # current_app.logger.info(f'product count is {count}, type is {type(count)}')
    return jsonify({"data": {"count": count,
                             "week": 10,
                             "day": -15},
                    "status": 0})


@overview_bp.get("/graph")
def overview_graph_view():
    is_visit: str = request.args.get("isVisited")
    visit_data = [35, 43, 38, 45, 61, 72, 65, 62, 50, 29, 21, 45]
    sales_data = [10, 12, 89, 76, 54, 23, 87, 21, 43, 51, 37, 46]
    if is_visit == 'true':
        data = visit_data
    else:
        data = sales_data
    data = [{"year": f"{x + 1}月", "sales": data[x]} for x in range(12)]
    return jsonify({"data": data, "status": 0})


@overview_bp.get("/line")
def overview_line_view():
    mau_list = [7.3, 8.2, 6.4, 10.5, 11.2, 7.6, 4.8, 5.3, 9.2, 4.2, 8.3, 2.9]
    promotion_list = [6.2, 8.3, 3.6, 6.4, 5.9, 10.5, 4.6, 2.7, 3.8, 8.2, 6.2, 7.1]
    transaction_list = [5.2, 9.4, 7.4, 6.8, 10.2, 11.3, 14.6, 8.8, 6.5, 11.2, 12.2, 8.3]
    mon_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    data = [{"month": mon_list[x], "MAU": mau_list[x],
             "PROMOTION": promotion_list[x], "TRANSACTION": transaction_list[x]} for x in range(12)]
    return jsonify({"data": data, "status": 0})


@overview_bp.get("/task")
def task_list_view():
    # params = request.args
    # username: str = str(params.get("username"))
    resp = [
        {'status': '1', 'context': '新版本迭代会'},
        {'status': '1', 'context': '完成网站设计初版'},
        {'status': '0', 'context': '联调接口'},
        {'status': '1', 'context': '登录功能设计'}
    ]
    return jsonify({"data": resp, "status": 0})
