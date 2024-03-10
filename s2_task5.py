"""
Задание №5
📌 Создать страницу, на которой будет форма для ввода двух
чисел и выбор операции (сложение, вычитание, умножение
или деление) и кнопка "Вычислить"
📌 При нажатии на кнопку будет произведено вычисление
результата выбранной операции и переход на страницу с
результатом.
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        operation = request.form.get('operation')
        result = 0
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '/':
            result = num1 / num2
        elif operation == '*':
            result = num1 * num2
        # else:
        #     return 'данная операция не поддерживается!'
        return f'{num1} {operation} {num2} = {result}'
    return render_template('task5_calc.html')


if __name__ == '__main__':
    app.run(debug=True)
