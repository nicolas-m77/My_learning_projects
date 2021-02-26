"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
my_numbers = input('Введите набор чисел, разделенных пробелами: ')
with open('for_5.5.txt', 'w') as f:  # Создаем программно текстовой файл и записываем набор введенных чисел
    f.write(my_numbers)

summa = 0
with open('for_5.5.txt', 'r') as f:
    my_string = f.read()
    my_string = my_string.split()
    for number in my_string:
        summa += int(number)
print('Сумма чисел из файла:', summa)
