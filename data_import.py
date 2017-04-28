import xlrd
from init import app, db
from models import City

book = xlrd.open_workbook('area.xlsx')
nsheets = book.nsheets
print('总共有{}个sheet'.format(nsheets))

sh = book.sheet_by_index(2)
print("{}, 共{}行, {}列".format(sh.name, sh.nrows, sh.ncols))

keys = []
data = []
for rx in range(sh.nrows):
    item = {}
    row = sh.row_values(rx)
    if rx == 0:
        keys = sh.row_values(rx)
    else:
        for col_k, col_v in enumerate(row):
            item[keys[col_k]] = col_v
        data.append(item)

print(data)

with app.app_context():
    for record in data:
        city = City.query.filter_by(area=record['城市']).first()
        if not city:
            city = City(record['城市'])
        city.population = int(record['accrual_money'])
        db.session.add(city)

    db.session.commit()
