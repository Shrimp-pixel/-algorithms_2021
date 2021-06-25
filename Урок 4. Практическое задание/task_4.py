"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(ls: list):
    m = max(ls, key=ls.count)
    return f'Чаще всего встречается число {m}, ' \
           f'оно появилось в массиве {ls.count(m)} раз(а)'


# print(func_1())
# print(func_2())
# print(func_3(array))
print(timeit.timeit(
    "func_1()",
    globals=globals(),
    number=100000
))
print(timeit.timeit(
    "func_2()",
    globals=globals(),
    number=100000
))
print(timeit.timeit(
    "func_3(array)",
    globals=globals(),
    number=100000
))
"""
0.170425
0.1811319
0.13873779999999997
Первые две функции оказались медленнее чем третья функция. 
Третья функция оказалась самой быстрой. Отимизация проведена успешно.
"""
