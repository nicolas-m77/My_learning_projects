"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
print('Введите данные построчно: ')
with open('for_5.1.txt', 'w', encoding='UTF-8') as f:
    while True:
        my_string = input()
        if len(my_string) == 0:
            break
        my_string = my_string + '\n'
        f.write(my_string)
