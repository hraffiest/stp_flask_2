import csv
from __init__ import app
from config import Config
from models.models import db, Dish


with open('data.csv', 'r') as data:
    dishes_csv = csv.reader(data)
    dishes = list(dishes_csv)
    for row in dishes[1:]:
        dish = Dish(d_id=int(row[0]),
                    title=row[1],
                    price=row[2],
                    description=row[3],
                    picture=Config.PICTURE_PATCH + row[4],
                    cat_id=int(row[5]))
        with app.app_context():
            db.session.add(dish)

# import works only with commit in cycle 'for'. Why?
with app.app_context():
    db.session.commit()


