import time

from flask import request, g, current_app, jsonify
from utils.jwt_util import verify_jwt


def jwt_authentication():
    # 获取请求头中的token
    # Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twF
    # t5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg

    current_app.logger.info(f'*request path is {request.path}*')
    g.user_id = None
    token = request.headers.get('Authorization')
    if token is not None and token.startswith('Bearer '):
        token = token[7:]
        current_app.logger.info(f'token is {token}')
        # 验证token
        payload = verify_jwt(token)

        current_app.logger.info(f'payload is {payload}')

        if payload is not None:
            exp = payload.get('exp', 0)
            if exp < int(time.time()):
                return jsonify({"status": 1, "msg": "token expires"})
            # 保存到g对象中
            g.user_id = payload.get('user_id')
            g.menus = payload.get('menus')
        else:
            return jsonify({"status": 1, "msg": "invalid token"})
    else:
        current_app.logger.info(f'*request path is {request.path}*')
        if request.path != '/api/v1/login':
            return jsonify({"status": 1, "msg": "invalid token"})
