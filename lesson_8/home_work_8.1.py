"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, 
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
"""
import datetime


class Date:
    def __init__(self, my_date):
        self.my_date = my_date

    @classmethod
    def int_date(cls, x):
        y = x.split('-')
        y[0] = int(y[0])
        y[1] = int(y[1])
        y[2] = int(y[2])
        return y

    @staticmethod
    def date_check(m_list):
        day = m_list[0]
        month = m_list[1]
        year = m_list[2]
        month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        now = datetime.datetime.now()
        if month > 12:
            month = int(now.strftime('%m'))  # Если месяцев больше 12, будет показан текущий месяц
            print('Введено неверное значение даты: месяцев не может быть больше 12')
        if day > month_dict[month]:
            day = int(now.strftime('%d'))  # Если количество дней не соответствует месяцу,
            # будет показан текущий день месяца
            print('Количество дней не соответствует месяцу')
        if year > int(now.strftime('%Y')):  # Если указан год далее текущего, будет показана текущая дата
            day = int(now.strftime('%d'))
            month = int(now.strftime('%m'))
            year = int(now.strftime('%Y'))
            print('Год не может быть больше текущего')
        print(day, month, year)


date = input('Введите дату в формате «день-месяц-год» не далее текущей: ')
int_date = Date.int_date(date)
Date.date_check(int_date)
