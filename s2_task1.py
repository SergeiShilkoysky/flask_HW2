"""Задание №1
📌 Создать страницу, на которой будет кнопка "Нажми меня", при
нажатии на которую будет переход на другую страницу с
приветствием пользователя по имени.
"""

from flask import Flask, render_template, request, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task1_main.html')


@app.route('/submit/', methods=['GET', 'POST'])
# def submit(name=None):
def submit(name=None):
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    # return render_template(url_for('index', name=name))
    return render_template(url_for('index'))


# упрощенный вариант:
# @app.post('/post/')
# def post(name=None):
#     name = request.form.get('name')
#     return f'Hello {name}!'


if __name__ == '__main__':
    app.run(debug=True)
