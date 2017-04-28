from flask_admin.contrib.sqla import ModelView

class CityView(ModelView):
    can_create = True
    can_delete = True
    can_edit = True
    can_export = True


