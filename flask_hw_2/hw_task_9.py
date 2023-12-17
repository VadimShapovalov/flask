# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке которой будет создан
# cookie-файл с данными пользователя, а также будет произведено перенаправление на страницу приветствия, где будет
# отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными
# пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, redirect, url_for, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        response = make_response(redirect(url_for('greet', name=name)))
        response.set_cookie('user_data', f'{name}:{email}')
        return response
    else:
        return render_template('login.html')


@app.route('/greet/<name>')
def greet(name: str):
    return render_template('greet.html', name=name)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('user_data')
    return response


if __name__ == '__main__':
    app.run(debug=True)