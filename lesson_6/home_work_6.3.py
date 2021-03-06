"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):


    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


first_worker = Position('Вася', 'Пупкин', 'штукатур-маляр', 30_000, 15_000)
second_worker = Position('Гоша', 'Куценко', 'актер', 300_000, 150_000)

# Вызываем методы экземплятров:
print(f'{first_worker.get_full_name()}, зарплата составляет {first_worker.get_total_income()} рублей')
# Проверяем значения атрибутов:
print(first_worker.name)
print(first_worker.surname)
print(first_worker.position)
print(first_worker._income['wage'], first_worker._income['bonus'])

print(f'{second_worker.get_full_name()}, зарплата составляет {second_worker.get_total_income()} рублей')
print(second_worker.name)
print(second_worker.surname)
print(second_worker.position)
print(second_worker._income['wage'], second_worker._income['bonus'])
