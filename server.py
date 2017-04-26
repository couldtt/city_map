import random
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = '#!@$@#$^@#^@#$&'
db = SQLAlchemy(app)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(64), unique=True)
    population = db.Column(db.Integer, nullable=False, default=0)


class CityView(ModelView):
    can_create = True
    can_delete = True
    can_edit = True
    can_export = True


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
