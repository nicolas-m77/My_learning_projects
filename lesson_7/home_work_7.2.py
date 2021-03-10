"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name.title()

    @abstractmethod
    def consumption(self):
        ...


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v
        self.param = 'размер'

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h
        self.param = 'рост'

    @property
    def consumption(self):
        return 2 * self.h + 0.3


my_suit = Suit('костюм', 170)
my_coat = Coat('пальто', 50)
print(f'Изделие: {my_suit.name}, {my_suit.param}: {my_suit.h}, расход ткани: {my_suit.consumption}')
print(f'Изделие: {my_coat.name}, {my_coat.param}: {my_coat.v}, расход ткани: {my_coat.consumption:.4f}')
print(f'Общий расход ткани: {(my_suit.consumption + my_coat.consumption):.4f}')
