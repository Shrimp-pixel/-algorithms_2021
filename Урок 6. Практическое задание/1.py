# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
import memory_profiler
from memory_profiler import profile, memory_usage
from pympler import asizeof


def decorator(func):
    def wrapper():
        m1 = memory_usage()
        func()
        m2 = memory_usage()
        print("memory_usage:", m2[0] - m1[0])

    return wrapper


@profile
def var1():
    class Road:
        def __init__(self, length, width):
            self._length = length
            self._width = width

        def calculate(self, mass, a):
            return self._length * self._width * mass * a

    road = Road(20, 5000)
    print(road.calculate(25, 5))
    print("Размер без использования slots", asizeof.asizeof(road))


@profile
def var2():
    class Road:
        __slots__ = ['_length', '_width']

        def __init__(self, length, width):
            self._length = length
            self._width = width

        def calculate(self, mass, a):
            return self._length * self._width * mass * a

    road = Road(20, 5000)
    print(road.calculate(25, 5))
    print("Размер при использование slots", asizeof.asizeof(road))
    del road


decorator(var1)()
decorator(var2)()

"""
12500000
Размер без использования slots 328

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    23     31.5 MiB     31.5 MiB           1   @profile
    24                                         def var1():
    25     31.5 MiB      0.0 MiB           3       class Road:
    26     31.5 MiB      0.0 MiB           2           def __init__(self, length, width):
    27     31.5 MiB      0.0 MiB           1               self._length = length
    28     31.5 MiB      0.0 MiB           1               self._width = width
    29                                         
    30     31.5 MiB      0.0 MiB           2           def calculate(self, mass, a):
    31     31.5 MiB      0.0 MiB           1               return self._length * self._width * mass * a
    32                                         
    33     31.5 MiB      0.0 MiB           1       road = Road(20, 5000)
    34     31.5 MiB      0.0 MiB           1       print(road.calculate(25, 5))
    35     31.6 MiB      0.0 MiB           1       print("Размер без использования slots", asizeof.asizeof(road))


memory_usage: 0.34375
12500000
Размер при использование slots 112

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    38     31.6 MiB     31.6 MiB           1   @profile
    39                                         def var2():
    40     31.6 MiB      0.0 MiB           3       class Road:
    41     31.6 MiB      0.0 MiB           1           __slots__ = ['_length', '_width']
    42                                         
    43     31.6 MiB      0.0 MiB           2           def __init__(self, length, width):
    44     31.6 MiB      0.0 MiB           1               self._length = length
    45     31.6 MiB      0.0 MiB           1               self._width = width
    46                                         
    47     31.6 MiB      0.0 MiB           2           def calculate(self, mass, a):
    48     31.6 MiB      0.0 MiB           1               return self._length * self._width * mass * a
    49                                         
    50     31.6 MiB      0.0 MiB           1       road = Road(20, 5000)
    51     31.6 MiB      0.0 MiB           1       print(road.calculate(25, 5))
    52     31.6 MiB      0.0 MiB           1       print("Размер при использование slots", asizeof.asizeof(road))
    53     31.6 MiB      0.0 MiB           1       del road


memory_usage: 0.0

Размер памяти занимаемым экземпляром класса Road уменьшился благодаря использованию slots

"""
