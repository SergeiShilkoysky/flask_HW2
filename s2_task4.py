"""
Задание №4
📌 Создать страницу, на которой будет форма для ввода текста и
кнопка "Отправить"
📌 При нажатии кнопки будет произведен подсчет количества слов
в тексте и переход на страницу с результатом.
"""

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def task4():
    if request.method == 'POST':
        name = request.form.get('text')
        return f'длина введенного текста >>> {str(len(name))}'
    return render_template('task4_send.html')


# @app.route('/length/<text>/')
# def text_length(text):
#     return str(len(text))


if __name__ == '__main__':
    app.run(debug=True)
