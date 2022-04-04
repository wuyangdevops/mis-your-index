from . import db


class Categories(db.Model):
    """
    category info model
    """

    __tablename__ = 'tb_categories'

    id = db.Column('id', db.BigInteger, primary_key=True, doc='category id')
    name = db.Column('name', db.String, doc='品类名称')
    parent_id = db.Column('parent_id', db.BigInteger, default='0', doc='密码')
    is_deleted = db.Column('is_deleted', db.Integer, default='0', doc='删除标识')
