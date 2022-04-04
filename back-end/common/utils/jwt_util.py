import time

import jwt
from flask import current_app


def generate_jwt(payload, expiry=None, secret=None):
    """
    生成jwt
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :param secret: 密钥
    :return: jwt
    """
    if expiry is None:
        expiry = int(time.time()) + 3600 * current_app.config['JWT_EXPIRY_HOURS']
    _payload = {'exp': expiry}
    _payload.update(payload)

    if not secret:
        secret = current_app.config['JWT_SECRET']

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token, expiry


def verify_jwt(token, secret=None):
    """
    检验jwt
    :param token: jwt
    :param secret: 密钥
    :return: dict: payload
    """
    if not secret:
        secret = current_app.config['JWT_SECRET']

    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
    except jwt.PyJWTError as e:
        current_app.logger.error(f'cannot decode, reason: {e}')
        payload = None

    return payload
