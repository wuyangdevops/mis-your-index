from flask import request
import logging
import logging.handlers
import os


class RequestFormatter(logging.Formatter):
    """
    针对请求信息的日志格式
    """
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def create_logger(app):
    """
    设置日志
    :param app: Flask app对象
    :return:
    """
    logging_file_dir = app.config['LOGGING_FILE_DIR']
    logging_file_max_bytes = app.config['LOGGING_FILE_MAX_BYTES']
    logging_file_backup = app.config['LOGGING_FILE_BACKUP']
    logging_level = app.config['LOGGING_LEVEL']

    flask_console_handler = logging.StreamHandler()
    flask_console_handler.setFormatter(logging.Formatter('%(levelname)s %(module)s %(lineno)d %(message)s'))

    request_formatter = RequestFormatter('[%(asctime)s] %(remote_addr)s requested %(url)s\n'
                                         '%(levelname)s in %(module)s %(lineno)d: %(message)s')

    flask_file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(logging_file_dir, 'flask.log'),
        maxBytes=logging_file_max_bytes,
        backupCount=logging_file_backup
    )
    flask_file_handler.setFormatter(request_formatter)
    log_flask_app = logging.getLogger('flask.app')
    log_flask_app.addHandler(flask_file_handler)
    log_flask_app.setLevel(logging_level)

    # if app.debug:
    log_flask_app.addHandler(flask_console_handler)
    app.logger = log_flask_app

