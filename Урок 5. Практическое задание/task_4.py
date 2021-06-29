"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
import timeit
from collections import OrderedDict

dc = {}
od = OrderedDict()


def filldc(d):
    for i in range(10000):
        d[i]=i
    return d


def fillod(o):
    for i in range(10000):
        o[i]=i
    return o


def popdc(d):
    newd=d.copy()
    for i in range(10000):
        newd.pop(i)
    return d


def popod(o):
    newo = o.copy()
    for i in range(10000):
        newo.pop(i)
    return o


def geteldc(d):
    for i in range(10000):
        x=d.get(i)
    return d


def getelod(o):
    for i in range(10000):
        x=o.get(i)
    return o


print("Fill: ")
print(timeit.timeit(
    "filldc(dc)",
    globals=globals(),
    number=1000
))
print(timeit.timeit(
    "fillod(od)",
    globals=globals(),
    number=1000
))


print("Get: ")
print(timeit.timeit(
    "geteldc(dc)",
    globals=globals(),
    number=1000
))
print(timeit.timeit(
    "getelod(od)",
    globals=globals(),
    number=1000
))


print("Pop: ")
print(timeit.timeit(
    "popdc(dc)",
    globals=globals(),
    number=1000
))
print(timeit.timeit(
    "popod(od)",
    globals=globals(),
    number=1000
))
"""
Fill: 
0.6698143000000001
1.0439667999999998
Get: 
0.8483513
0.8376070000000002
Pop: 
1.1427224999999996
3.2603817

Как видно из тестов pop выполняется медленее для OrderedDict.
Нет смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях т.к. dict уже упорядочен.
"""
