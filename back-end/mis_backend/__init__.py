from flask import Flask


def create_flask_app(config):
    """
    创建Flask应用
    :param config: 配置信息对象
    :return: Flask应用
    """
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def create_app(config):
    """
    创建应用
    :param config: 配置信息对象
    :return: 应用
    """
    app = create_flask_app(config)

    # 限流器
    from utils.limiter import limiter as lmt
    lmt.init_app(app)

    # 配置日志
    from utils.logging import create_logger
    create_logger(app)

    # MySQL数据库连接初始化
    from models import db

    db.init_app(app)

    # 添加请求钩子
    from utils.middlewares import jwt_authentication
    app.before_request(jwt_authentication)

    # 注册蓝图
    from .blueprints.users import user_bp
    app.register_blueprint(user_bp)
    from .blueprints.roles import role_bp
    app.register_blueprint(role_bp)
    from .blueprints.login import login_bp
    app.register_blueprint(login_bp)
    from .blueprints.categories import category_bp
    app.register_blueprint(category_bp)
    from .blueprints.products import product_bp
    app.register_blueprint(product_bp)
    from .blueprints.overview import overview_bp
    app.register_blueprint(overview_bp)

    return app
