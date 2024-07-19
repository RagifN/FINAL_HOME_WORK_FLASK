from flask import Flask, render_template
from models import db, Users, TheGoods

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('NICE')


@app.cli.command('user-db')
def add_data():
    for i in range(1, 4):
        the_goods = TheGoods(
            name=f'goods_{i}'
        )
        db.session.add(the_goods)

    for i in range(0, 10):
        user = Users(
            firstname=f'firstname{i}',
            lastname=f'lastname{i}',
            email=f'{i}@gmail.com',
            password=f'{i}123')
        db.session.add(user)
    db.session.commit()
    print("Datas added")


@app.get('/')
def get_student():
    users = Users.query.all()
    context = {
        'students': users
    }
    return render_template('index.html', **context)