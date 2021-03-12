"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить 
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.
"""


class Stock:
   ...


class OfficeEquipment:
    def __init__(self, name, maker, year):
        self.name = name.title()
        self.maker = maker.upper()
        self.year = year


class Printer(OfficeEquipment):
    def __init__(self, name, maker, year, performance, param):
        self.performance = performance
        self.param = param
        super().__init__(name, maker, year)


class Copier(OfficeEquipment):
    def __init__(self, name, maker, year, speed, param):
        self.speed = speed
        self.param = param
        super().__init__(name, maker, year)


class Scanner(OfficeEquipment):
    def __init__(self, name, maker, year, resolution, param):
        self.resolution = resolution
        self.param = param
        super().__init__(name, maker, year)


my_scanner = Scanner('сканер', 'canon', 2015, 600, 'dpi')
my_printer = Printer('принтер', 'hp', 2018, 1500, 'p')
my_copier = Copier('ксерокс', 'samsung', 2014, 20, 'p/m')
print('На складе находится следующее оборудование:')
print(my_printer.name, my_printer.maker, my_printer.year, my_printer.performance, my_printer.param)
print(my_copier.name, my_copier.maker, my_copier.year, my_copier.speed, my_copier.param)
print(my_scanner.name, my_scanner.maker, my_scanner.year, my_scanner.resolution, my_scanner.param)
