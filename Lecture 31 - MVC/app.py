from flask import Flask, render_template, request, redirect, url_for
from models import db, Car
from flask_cors import CORS

app = Flask(__name__)


CORS(app)

host = 'localhost'
port = '5432'
user = 'postgres'
password = '123123'
database = 'flask'


app.secret_key = 'SecretKey'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{database}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    all_cars = Car.query.all()
    return render_template('index.html', cars=all_cars)


@app.route('/insert', methods=['GET', 'POST'])
def insert():

    if request.method == 'POST':

        manufacturer = request.form['manufacturer']
        model = request.form['model']
        instock = request.form['instock']
        price = request.form['price']

        new_car = Car(manufacturer, model, instock, price)
        db.session.add(new_car)
        db.session.commit()


        return  redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
