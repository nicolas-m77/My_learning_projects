"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name.title()
        self.is_police = False
        self.direction = 'пока прямо'

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {self.direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super(TownCar, self).__init__(speed, color, name)
        self.is_police = False
        self.direction = 'пока прямо'

    def show_speed(self):
        print(f'Скорость машины {self.name}: {self.speed} км/ч')
        if self.speed > 60:
            print('Скорость превышена')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super(SportCar, self).__init__(speed, color, name)
        self.is_police = False
        self.direction = 'пока прямо'


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super(WorkCar, self).__init__(speed, color, name)
        self.is_police = False
        self.direction = 'пока прямо'

    def show_speed(self):
        print(f'Скорость машины {self.name}: {self.speed} км/ч')
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super(PoliceCar, self).__init__(speed, color, name)
        self.is_police = True
        self.direction = 'пока прямо'


my_car = Car(65, 'красный', 'жигули')
my_car.go()
my_car.turn('направо')
print('Направление движения:', my_car.direction)
my_car.show_speed()
my_car.stop()
print(f'Полиция?', my_car.is_police)
print(f'Цвет машины {my_car.color}')

my_police = PoliceCar(80, 'синий', 'полиция')
print(my_police.name)
print('Направление движения:', my_police.direction)
my_police.show_speed()
print(f'Полиция?', my_police.is_police)

my_work_car = WorkCar(65, 'оранжевый', 'зил')
print(my_work_car.name)
my_work_car.show_speed()

