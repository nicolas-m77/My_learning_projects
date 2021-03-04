"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    def __init__(self, color='Мигающий желтый'):
        self.color = color

    def running(self):
        print(f'Горит {self.color} свет')


my_traffic = TrafficLight()

while True:
    my_traffic.color = 'Красный'
    my_traffic.running()
    for i in range(1, 8):
        time.sleep(1)
        print(i)
    my_traffic.color = 'Желтый'
    my_traffic.running()
    for i in range(1, 3):
        time.sleep(1)
        print(i)
    my_traffic.color = 'Зеленый'
    my_traffic.running()
    for i in range(1, 11):
        time.sleep(1)
        print(i)
