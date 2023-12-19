from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms_4 import Registration
from models_4 import User, db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def login1():
    form = Registration()
    form_errors = []
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        if User.query.filter(User.username == username).count() > 0:
            form_errors.append('Username is taken')
        if User.query.filter(User.email == email).count() > 0:
            form_errors.append('Email is taken')
        else:
            add_user(username, email, form.password.data) # form.email.data
            form_notifications = [f'User {username} successfully added']
            print(f'Добавлен пользователь: {username} {email}')
            return render_template('login1.html', form=form, form_notifications=form_notifications)
    return render_template('login1.html', form=form, form_errors=form_errors)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Database created')


if __name__ == '__main__':
    app.run(debug=True)
