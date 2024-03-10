"""
Задание №6
📌 Создать страницу, на которой будет форма для ввода имени
и возраста пользователя и кнопка "Отправить"
📌 При нажатии на кнопку будет произведена проверка
возраста и переход на страницу с результатом или на
страницу с ошибкой в случае некорректного возраста.
"""

from flask import Flask, request, render_template, abort
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

AGE = '30'


@app.route('/', methods=['GET', 'POST'])
def check_age():
    if request.method == 'POST':
        age = request.form.get('age')
        name = request.form.get('name')
        if age == AGE:
            return f'Hello {name}, whoes age {AGE}!'
        return abort(403)
    return render_template('task6_check_age.html')


@app.errorhandler(403)
def access_denied(err):
    logger.warning(err)
    context = {
        'title': '403 Forbidden',
        'comment': 'Ошибка доступа!',
    }
    return render_template('task6_error.html', **context), 403


if __name__ == '__main__':
    app.run(debug=True)
