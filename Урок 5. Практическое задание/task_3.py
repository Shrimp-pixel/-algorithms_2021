"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
import timeit
from collections import deque

ls = []
dq = deque()


def fillls(l):
    for i in range(10000):
        l.append(i)
    return l


def filldq(d):
    for i in range(10000):
        d.append(i)
    return d


def appendleftls(l):
    for i in range(1000):
        l.insert(0, i)
    return l


def appendleftdq(d):
    for i in range(1000):
        d.appendleft(i)
    return d


def popls(l):
    for i in range(10000):
        l.pop()
    return l


def popdq(d):
    for i in range(10000):
        d.pop()
    return d


def popleftls(l):
    newl = l.copy()
    for i in range(10000):
        newl.pop(0)
    return l


def popleftdq(d):
    newd = d.copy()
    for i in range(10000):
        newd.popleft()
    return d


def extendls(l):
    l.extend([i for i in range(1000)])
    return l


def extenddq(d):
    d.extend([i for i in range(1000)])
    return d


print("Fill: ")
print(timeit.timeit(
    "fillls(ls)",
    globals=globals(),
    number=1000
))
print(timeit.timeit(
    "filldq(dq)",
    globals=globals(),
    number=1000
))

print("pop: ")
print(timeit.timeit(
    "popls(ls)",
    globals=globals(),
    number=1000
))
print(timeit.timeit(
    "popdq(dq)",
    globals=globals(),
    number=1000
))

print("appendleft: ")
print(timeit.timeit(
    "appendleftls(ls)",
    globals=globals(),
    number=100
))
print(timeit.timeit(
    "appendleftdq(dq)",
    globals=globals(),
    number=100
))

ls = fillls(ls)
dq = filldq(dq)

print("popleft: ")
print(timeit.timeit(
    "popleftls(ls)",
    globals=globals(),
    number=100
))
print(timeit.timeit(
    "popleftdq(dq)",
    globals=globals(),
    number=100
))

print("extend: ")
print(timeit.timeit(
    "extendls(ls)",
    globals=globals(),
    number=1000
))
print(timeit.timeit(
    "extenddq(dq)",
    globals=globals(),
    number=1000
))

"""
Fill: 
0.9352461
0.8897972000000001
pop: 
0.8084302999999999
0.743446
appendleft: 
4.0032648
0.008087300000000575
popleft: 
34.798369900000004
0.20497010000000415
extend: 
0.08289349999999729
0.05269489999999877

Скорость заполнения, pop и extend у deque и list примерно одинаковая.
Однако скорость appendleft, popleft у deque и list отличается во много раз.
Deque оказался быстрее чем list во всех сравнениях. 
"""
