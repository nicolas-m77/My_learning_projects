"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно 
обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyError(Exception):

    def __init__(self, some_text):
        self.some_text = some_text


def division(a, b):
    try:
        if b == 0:
            raise MyError('Попытка деления на ноль, деление невозможно!')
        else:
            return a / b
    except MyError as e:
        return e


print('Сейчас трижды будет совершено деление введенных Вами чисел.\n')
for i in range(3):
    dividend = int(input('Введите делимое: '))
    divisor = int(input('Введите делитель: '))
    print(f'Результат деления первого числа на второе: {division(dividend, divisor)}\n')
