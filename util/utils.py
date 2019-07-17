import functools
import json
from datetime import datetime
from datetime import date
from decimal import Decimal


def log(t):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s() begin' % (t, func.__name__))
            r = func(*args, **kw)
            print('end')
            return r
        return wrapper
    return decorator


class ApiResult(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setdefault('code', 0)
        self.setdefault('msg', '')
        self.setdefault('data', None)


class WebJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.__str__()
        if isinstance(obj, datetime):
            return obj.__str__()
        if isinstance(obj, Decimal):
            return obj.__str__()
        if isinstance(obj, ApiResult):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)