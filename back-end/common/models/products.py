from . import db


class Products(db.Model):
    """
    product info model
    """

    __tablename__ = 'tb_products'

    id = db.Column('id', db.BigInteger, primary_key=True, doc='product id')
    name = db.Column('name', db.String, doc='商品名称')
    desc = db.Column('desc', db.String, default='', doc='商品描述')
    price = db.Column('price', db.DECIMAL(10, 2), default='0.00', doc='商品价格')
    parent_category_id = db.Column('parent_category_id', db.BigInteger, default='0', doc='一级类别ID')
    category_id = db.Column('category_id', db.BigInteger, default='0', doc='二级类别ID')
    on_sale = db.Column('on_sale', db.SmallInteger, default='1', doc='上架状态')
    is_deleted = db.Column('is_deleted', db.Integer, default='0', doc='删除标识')
