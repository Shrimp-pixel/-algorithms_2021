"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import operator
import timeit
import random


def semidec(fun, ls):
    print("Исходный -", ls)
    res = fun(ls)
    print("Отсортированный -", res)
    return res


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


def another_merge_sort(L, compare=operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = another_merge_sort(L[:middle], compare)
        right = another_merge_sort(L[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


orig_list = [random.randint(0, 50) for _ in range(int(input("Введите число элементов: ")))]
semidec(merge_sort, orig_list[:])
semidec(another_merge_sort, orig_list[:])

for i in [pow(10, h) for h in range(1, 5)]:
    ls = [random.randint(0, 50) for _ in range(i)]
    print("Number:", i)
    print(
        timeit.timeit(
            "merge_sort(ls[:])",
            globals=globals(),
            number=1000))
    print(
        timeit.timeit(
            "another_merge_sort(ls[:])",
            globals=globals(),
            number=1000))

"""
Введите число элементов: 25
Исходный - [7, 47, 37, 28, 19, 48, 47, 1, 2, 6, 31, 1, 31, 16, 15, 6, 16, 5, 39, 35, 29, 5, 2, 28, 45]
Отсортированный - [1, 1, 2, 2, 5, 5, 6, 6, 7, 15, 16, 16, 19, 28, 28, 29, 31, 31, 35, 37, 39, 45, 47, 47, 48]
Исходный - [7, 47, 37, 28, 19, 48, 47, 1, 2, 6, 31, 1, 31, 16, 15, 6, 16, 5, 39, 35, 29, 5, 2, 28, 45]
Отсортированный - [1, 1, 2, 2, 5, 5, 6, 6, 7, 15, 16, 16, 19, 28, 28, 29, 31, 31, 35, 37, 39, 45, 47, 47, 48]
Number: 10
0.013074699999999773
0.013961199999999785
Number: 100
0.1730765999999999
0.22608490000000003
Number: 1000
2.5317054
2.8605556000000005
Number: 10000
35.662787599999994
42.8049228
"""
