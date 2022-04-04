import pymysql
pymysql.install_as_MySQLdb()

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
