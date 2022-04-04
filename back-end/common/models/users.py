from datetime import datetime

from . import db


class Users(db.Model):
    """
    user info model
    """

    __tablename__ = 'tb_users'

    id = db.Column('id', db.BigInteger, primary_key=True, doc='user id')
    username = db.Column('username', db.String, doc='用户名')
    password = db.Column('password', db.String, doc='密码')
    is_deleted = db.Column('is_deleted', db.BigInteger, default='0', doc='删除标识')
    role_id = db.Column('role_id', db.BigInteger, default='0', doc='权限id')
    email = db.Column('email', db.String, default='', doc='用户email')
    phone = db.Column('phone', db.String, default='', doc='手机号')
    create_time = db.Column('create_time', db.DateTime, default=datetime.now, doc='创建时间')
