"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title.title()

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print(f'Концелярская принадлежность: {self.title}, отрисовка запущена')


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print(f'Концелярская принадлежность: {self.title}, отрисовка началась')


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print(f'Концелярская принадлежность: {self.title}, отрисовка пошла')


my_stationery = Stationery('перо')
print(my_stationery.title)
my_stationery.draw()

my_pen = Pen('ручка')
print(my_pen.title)
my_pen.draw()

my_pencil = Pencil('карандаш')
print(my_pencil.title)
my_pencil.draw()

my_hadle = Handle('маркер')
print(my_hadle.title)
my_hadle.draw()
