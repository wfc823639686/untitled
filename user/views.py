import datetime
import json

from user.models import User
from ormplus import orm
from util.utils import ApiResult

# Create your views here.


def save_or_upd(request):
    user = User()
    user.set_dict(json.loads(request.body.decode()))
    user.insert()
    current_time = datetime.datetime.now()
    return ApiResult(code= 1, msg='save error', data=current_time)


def user_list(request):
    sql = """
            select * from t_user
            where 1=1
            {and us_name = #name#}
        """
    r = orm.select_list(sql, request.GET, ["ps['name'] != None"], cl=User)
    return r