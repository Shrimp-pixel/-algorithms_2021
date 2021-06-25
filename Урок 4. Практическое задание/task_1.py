"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def fun2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


test = [i for i in range(100)]
print(timeit.timeit(
    "func_1(test)",
    globals=globals(),
    number=1000000
))
print(timeit.timeit(
    "fun2(test)",
    globals=globals(),
    number=1000000
))
"""
9.300183599999999
7.327389099999998
fun2 использует List comprehension т.к. это функция работает быстрее чем func_1.
fun2 работает на 23% быстрее чем func_1
"""
