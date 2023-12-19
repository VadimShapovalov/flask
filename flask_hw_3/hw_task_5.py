from flask import Flask, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

from forms_5 import RegistrationForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
csrf = CSRFProtect(app)

us = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RegistrationForm()
    form_notifications = []
    if request.method == 'POST' and form.validate():
        us['username'] = form.name.data
        us['email'] = form.email.data
        us['password'] = form.password.data
        us['birth_date'] = form.birth_date.data
        us['data_access'] = form.data_access.data
        user = form.data.copy()

        form_notifications.append(
            f'User {user["name"]} successfully registered!'
        )
        print(f"{us['username']}")
        return redirect(url_for('main', username=us['username']))
    return render_template('login2.html', form=form )


@app.route('/<username>/')
def main(username: str):
    return render_template('register.html', **us)


if __name__ == '__main__':
    app.run(debug=True)
