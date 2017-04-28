from init import app, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from models import City


class CityView(ModelView):
    can_create = True
    can_delete = True
    can_edit = True
    can_export = True


admin = Admin(app, name='CityMap', template_mode='bootstrap3')
admin.add_view(CityView(City, db.session, name='地域设置', category='区域分析'))
