from ormplus import orm

# Create your models here.


class User(orm.Model):
    table_name = 't_user'
    us_id = orm.IntegerField('id', primary=True)
    us_name = orm.StringField('name', notnull=False)