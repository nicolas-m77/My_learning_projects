"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.complex = complex(real, imaginary)

    def __add__(self, other):
        return self.complex + other.complex

    def __mul__(self, other):
        return self.complex * other.complex


a = int(input('Введите вещественную часть первого комплексного числа: '))
b = int(input('Введите мнимую часть первого комплексного числа: '))
c = int(input('Введите вещественную часть второго комплексного числа: '))
d = int(input('Введите мнимую часть второго комплексного числа: '))
complex_number_1 = ComplexNumber(a, b)
complex_number_2 = ComplexNumber(c, d)
print('Первое введенное число:', complex_number_1.complex)
print('Второе комплексное число:', complex_number_2.complex)
print('Результат сложения чисел:', complex_number_1 + complex_number_2)
print('Результат произведения чисел:', complex_number_1 * complex_number_2)
