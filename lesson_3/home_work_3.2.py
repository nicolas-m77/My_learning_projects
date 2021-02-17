"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def user_data(name, last_name, born, city, mail, phone):

    return dict(имя=name, фамилия=last_name, год=born, город=city, email=mail, телефон=phone)


user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_born = int(input("Введите год рождения: "))
user_city = input("Введите город проживания: ")
user_mail = input("Введите email: ")
user_phone = input("Введите номер телефона: ")

print(user_data(name=user_name, last_name=user_surname, born=user_born, city=user_city,
                mail=user_mail, phone=user_phone))
