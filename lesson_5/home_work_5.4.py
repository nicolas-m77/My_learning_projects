"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
n = 0
with open('for_5.4.txt', 'r', encoding='utf-8') as file:
    for line in file:
        my_string = line.split()
        if my_string[0] == 'One':
            my_string[0] = 'Один'
        elif my_string[0] == 'Two':
            my_string[0] = 'Два'
        elif my_string[0] == 'Three':
            my_string[0] = 'Три'
        elif my_string[0] == 'Four':
            my_string[0] = 'Четыре'
        new_string = " ".join(my_string)
        with open('new_for_5.4.txt', 'a', encoding='utf-8') as new_file:
            new_file.write(new_string)
            n += 1
            if n == 4:  # Убираем лишний перенос строк после 4 строки
                break
            new_file.write('\n')
