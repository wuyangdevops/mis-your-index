import time


def gen_timestamp() -> int:
    return int(time.time() * 1000)
