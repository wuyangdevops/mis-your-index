from datetime import datetime

from . import db


class Roles(db.Model):
    """
    role info model
    """

    __tablename__ = 'tb_roles'

    id = db.Column('id', db.BigInteger, primary_key=True, doc='user id')
    name = db.Column('name', db.String, doc='角色名称')
    auth_name = db.Column('auth_name', db.String, default='', doc='授权人')
    is_deleted = db.Column('is_deleted', db.BigInteger, default='0', doc='删除标识')
    menus = db.Column('menus', db.String, default='', doc='授权目录')
    create_time = db.Column('create_time', db.DateTime, default=datetime.now, doc='创建时间')
    auth_time = db.Column('auth_time', db.DateTime, default=datetime.now, onupdate=datetime.now, doc='授权时间')
