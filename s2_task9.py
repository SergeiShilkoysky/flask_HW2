"""
Задание №9
📌 Создать страницу, на которой будет форма для ввода имени
и электронной почты
📌 При отправке которой будет создан cookie файл с данными
пользователя
📌 Также будет произведено перенаправление на страницу
приветствия, где будет отображаться имя пользователя.
📌 На странице приветствия должна быть кнопка "Выйти"
📌 При нажатии на кнопку будет удален cookie файл с данными
пользователя и произведено перенаправление на страницу
ввода имени и электронной почты.
"""

from flask import (Flask, render_template, request, make_response,
                   session, redirect, url_for)

app = Flask(__name__)

app.secret_key = '8046141b685a85b0c6b1b00139c0f7d516a5c8d0eb7ae56a9d4e1f6bd5aed932'


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/form/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        resp = make_response(redirect(url_for('profile')))
        resp.set_cookie('user', name)
        resp.set_cookie('mail', email)
        return resp
    return render_template('task9_user_form.html')


@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        resp = make_response(redirect(url_for('home')))
        resp.delete_cookie('user')
        resp.delete_cookie('mail')
        return resp
    if request.cookies.get('user'):
        return render_template('task9_personal_profile.html',
                               name=request.cookies.get('user'))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
