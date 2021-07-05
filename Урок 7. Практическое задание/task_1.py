"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import random
import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def better_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = False
        if flag:
            break
        n += 1
    return lst_obj


l = 25
ls = []
for _ in range(l):
    ls.append(random.randint(-100, 100))

print(
    timeit.timeit(
        "bubble_sort(ls[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "better_bubble_sort(ls[:])",
        globals=globals(),
        number=1000))

"""
0.08120550000000001
0.034470399999999984

better_bubble_sort работает быстрее чем bubble_sort из-за добавления flag. Если в цикле перестановок не было то,
значит list отсортирован и нет смысла продолжать. """