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

with open('for_5.4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        my_list = line.split()
        if my_list[0] == 'One':
            my_list[0] = 'Один'
        elif my_list[0] == 'Two':
            my_list[0] = 'Два'
        elif my_list[0] == 'Three':
            my_list[0] = 'Три'
        elif my_list[0] == 'Four':
            my_list[0] = 'Четыре'
        new_string = " ".join(my_list)
        with open('new_for_5.4.txt', 'a', encoding='utf-8') as new_f:
            new_f.write(new_string)
            new_f.write('\n')  # Записываем перенос строки в конец каждой строки
