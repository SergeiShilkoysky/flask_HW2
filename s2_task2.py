"""
Задание №2
📌 Создать страницу, на которой будет изображение и ссылка
на другую страницу, на которой будет отображаться форма
для загрузки изображений.
"""

from pathlib import PurePath, Path

from flask import Flask, render_template, request
from markupsafe import escape
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('task2_main.html')


@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        file = request.files.get("file")
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), "task2_uploads", file_name))
        return f"Файл {file_name} загружен на сервер"
    # следущий код выполняется при методе запроса GET
    return render_template('task2_upload.html')


if __name__ == '__main__':
    app.run(debug=True)
