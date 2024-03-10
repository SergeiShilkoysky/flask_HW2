"""Задание №3
📌 Создать страницу, на которой будет форма для ввода логина
и пароля
📌 При нажатии на кнопку "Отправить" будет произведена
проверка соответствия логина и пароля и переход на
страницу приветствия пользователя или страницу с
ошибкой.
"""

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

LOGIN = 'admin'
PASS = '1'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        login = request.form.get("login")
        password = request.form.get("password")
        if login == LOGIN and password == PASS:
            # return render_template(url_for("task3_index.html"))
            #  return render_template(url_for("task3_index.html", name=login)) # не работает!!!
            return render_template("task3_index.html", name=login)

        else:
            return render_template("task3_404.html")
            # более простой вариант с открытием отдельной страницы (переход на др. адрес)
            # return redirect(url_for('static', filename="task3_404.html"))
    return render_template("task3_login.html")


# менеджер контекстов
with app.test_request_context('/', method='POST'):
    assert request.path == '/'
    assert request.method == 'POST'

if __name__ == '__main__':
    app.run(debug=True)
