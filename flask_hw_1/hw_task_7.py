from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = [
        {'title': 'News1',
         'news': 'Теперь все будет хорошо!',
         'date': '01.12.23'},
        {'title': 'News2',
         'news': 'Теперь все будет еще лучше!',
         'date': '03.12.23'},
        {'title': 'News3',
         'news': 'Лучше просто не бывает!',
         'date': '05.12.23'},
    ]
    return render_template('main.html', context=context)


if __name__ == '__main__':
    app.run(debug=True)