import hashlib


def calc_sha1(password):
    sha1_obj = hashlib.sha1()
    sha1_obj.update(password.encode('utf-8'))
    return sha1_obj.hexdigest()
