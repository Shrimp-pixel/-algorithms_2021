# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
from numpy import array
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
    a = list(input("Введите список "))
    print("Размер при использование list", asizeof.asizeof(a))
    print("Введенный список:", a)
    if len(a) % 2 == 0:
        for i in range(0, len(a), 2):
            print(i, a)
            x = a[i]
            a[i] = a[i + 1]
            a[i + 1] = x
    else:
        for i in range(0, len(a) - 1, 2):
            x = a[i]
            a[i] = a[i + 1]
            a[i + 1] = x
    print("Результат:", a)


@profile
def var2():
    a = array(list(input("Введите список ")))
    print("Размер при использование numpy", asizeof.asizeof(a))
    print("Введенный список:", a)
    if len(a) % 2 == 0:
        for i in range(0, len(a), 2):
            print(i, a)
            x = a[i]
            a[i] = a[i + 1]
            a[i + 1] = x
    else:
        for i in range(0, len(a) - 1, 2):
            x = a[i]
            a[i] = a[i + 1]
            a[i + 1] = x
    print("Результат:", a)
    del a


decorator(var1)()
decorator(var2)()
"""
Введите список 12345678
Размер при использование list 568
Введенный список: ['1', '2', '3', '4', '5', '6', '7', '8']
0 ['1', '2', '3', '4', '5', '6', '7', '8']
2 ['2', '1', '3', '4', '5', '6', '7', '8']
4 ['2', '1', '4', '3', '5', '6', '7', '8']
6 ['2', '1', '4', '3', '6', '5', '7', '8']
Результат: ['2', '1', '4', '3', '6', '5', '8', '7']

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     31.5 MiB     31.5 MiB           1   @profile
    21                                         def var1():
    22     31.5 MiB      0.0 MiB           1       a = list(input("Введите список "))
    23     31.5 MiB      0.0 MiB           1       print("Размер при использование list", asizeof.asizeof(a))
    24     31.5 MiB      0.0 MiB           1       print("Введенный список:", a)
    25     31.5 MiB      0.0 MiB           1       if len(a) % 2 == 0:
    26     31.5 MiB      0.0 MiB           5           for i in range(0, len(a), 2):
    27     31.5 MiB      0.0 MiB           4               print(i, a)
    28     31.5 MiB      0.0 MiB           4               x = a[i]
    29     31.5 MiB      0.0 MiB           4               a[i] = a[i + 1]
    30     31.5 MiB      0.0 MiB           4               a[i + 1] = x
    31                                             else:
    32                                                 for i in range(0, len(a) - 1, 2):
    33                                                     x = a[i]
    34                                                     a[i] = a[i + 1]
    35                                                     a[i + 1] = x
    36     31.5 MiB      0.0 MiB           1       print("Результат:", a)


memory_usage: 0.390625
Введите список 12345678
Размер при использование numpy 144
Введенный список: ['1' '2' '3' '4' '5' '6' '7' '8']
0 ['1' '2' '3' '4' '5' '6' '7' '8']
2 ['2' '1' '3' '4' '5' '6' '7' '8']
4 ['2' '1' '4' '3' '5' '6' '7' '8']
6 ['2' '1' '4' '3' '6' '5' '7' '8']
Результат: ['2' '1' '4' '3' '6' '5' '8' '7']

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    39     31.5 MiB     31.5 MiB           1   @profile
    40                                         def var2():
    41     31.5 MiB      0.0 MiB           1       a = array(list(input("Введите список ")))
    42     31.6 MiB      0.0 MiB           1       print("Размер при использование numpy", asizeof.asizeof(a))
    43     31.6 MiB      0.0 MiB           1       print("Введенный список:", a)
    44     31.6 MiB      0.0 MiB           1       if len(a) % 2 == 0:
    45     31.6 MiB      0.0 MiB           5           for i in range(0, len(a), 2):
    46     31.6 MiB      0.0 MiB           4               print(i, a)
    47     31.6 MiB      0.0 MiB           4               x = a[i]
    48     31.6 MiB      0.0 MiB           4               a[i] = a[i + 1]
    49     31.6 MiB      0.0 MiB           4               a[i + 1] = x
    50                                             else:
    51                                                 for i in range(0, len(a) - 1, 2):
    52                                                     x = a[i]
    53                                                     a[i] = a[i + 1]
    54                                                     a[i + 1] = x
    55     31.6 MiB      0.0 MiB           1       print("Результат:", a)
    56     31.6 MiB      0.0 MiB           1       del a


memory_usage: 0.015625

Размер памяти занимаемым объектом 'a' уменьшился благодаря использованию numpy.array вместо list.

"""
