from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        number = float(request.form.get('number'))
        square = number ** 2
        return render_template('result.html', number=number, square=square)


if __name__ == '__main__':
    app.run(debug=True)
