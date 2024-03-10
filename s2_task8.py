"""
Задание №8
📌 Создать страницу, на которой будет форма для ввода имени
и кнопка "Отправить"
📌 При нажатии на кнопку будет произведено
перенаправление на страницу с flash сообщением, где будет
выведено "Привет, {имя}!".
"""

from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = '8046141b685a85b0c6b1b00139c0f7d516a5c8d0eb7ae56a9d4e1f6bd5aed932'


# >>> import secrets
# >>> secrets.token_hex()

@app.route('/', methods=['GET', 'POST'])
def flash_message():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Введите имя!', 'danger')
            return redirect(url_for('flash_message'))
        name = request.form.get('name')
        flash(f'Привет, {name}!', 'success')
        return redirect(url_for('flash_message'))
    return render_template('task8_flash.html')
    # return render_template('flash_form.html')


# функцию redirect() для перенаправления пользователя на главную страницу с
# # помощью функции url_for(), которая возвращает URL-адрес для указанного
# # маршрута.

if __name__ == '__main__':
    app.run(debug=True)
