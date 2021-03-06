import random
from flask import jsonify, render_template
from flask_admin import Admin

from init import app, db
from models import City
from admin import CityView


admin = Admin(app, name='CityMap', template_mode='bootstrap3')
admin.add_view(CityView(City, db.session, name='地域设置', category='区域分析'))

def processing(q):
    city_map = {}
    colors = ['red', 'black', 'blue', '#FF8811']
    for item in q:
        city_map[item.area] = colors[random.randint(0, 3)]

    return city_map


@app.route('/cities')
def cities():
    query = City.query
    city_map = processing(query)
    return jsonify(city_map)


@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    @app.before_first_request
    def create_db():
        db.create_all()


    app.run(debug=True)
