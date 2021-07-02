"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
"""
from pympler import asizeof
from recordclass import recordclass
from collections import namedtuple
from memory_profiler import profile, memory_usage


def decorator(func):
    def wrapper():
        m1 = memory_usage()
        func()
        m2 = memory_usage()
        print("memory_usage:", m2[0] - m1[0])

    return wrapper


@profile
def var1():
    num = int(input("Введите количество предприятий для расчета прибыли: "))
    ls = []
    company = namedtuple('Company', 'name income')
    income = 0
    for _ in range(num):
        ls.append(company(input("Введите название предприятия: "), input("через пробел введите прибыль данного "
                                                                         "предприятия за каждый квартал(Всего 4 "
                                                                         "квартала): ")))
        income = income + sum(int(h) for h in ls[-1].income.split())
    print("Размер при использование namedtuple", asizeof.asizeof(ls))
    income = float(income) / len(ls)
    lsmore = []
    lsless = []
    print("Средняя годовая прибыль всех предприятий:", income)
    for i in ls:
        s = sum(int(h) for h in i.income.split())
        if s > income:
            lsmore.append(i)
        elif s < income:
            lsless.append(i)

    print(f"Предприятия, с прибылью выше среднего значения: {', '.join([l.name for l in lsmore])}")
    print(f"Предприятия, с прибылью ниже среднего значения: {', '.join([l.name for l in lsless])}")


@profile
def var2():
    num = int(input("Введите количество предприятий для расчета прибыли: "))
    ls = []
    company = recordclass('Company', 'name income')
    income = 0
    for _ in range(num):
        ls.append(company(input("Введите название предприятия: "), input("через пробел введите прибыль данного "
                                                                         "предприятия за каждый квартал(Всего 4 "
                                                                         "квартала): ")))
        income = income + sum(int(h) for h in ls[-1].income.split())
    print("Размер при использование recordclass", asizeof.asizeof(ls))
    income = float(income) / len(ls)
    lsmore = []
    lsless = []
    print("Средняя годовая прибыль всех предприятий:", income)
    for i in ls:
        s = sum(int(h) for h in i.income.split())
        if s > income:
            lsmore.append(i)
        elif s < income:
            lsless.append(i)
    del ls
    print(f"Предприятия, с прибылью выше среднего значения: {', '.join([l.name for l in lsmore])}")
    del lsmore
    print(f"Предприятия, с прибылью ниже среднего значения: {', '.join([l.name for l in lsless])}")
    del lsless


decorator(var1)()
decorator(var2)()
"""
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: a1
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 1234 1234 1234 1234
Введите название предприятия: a2
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 4567 4567 4567 4567
Размер при использование namedtuple 456
Средняя годовая прибыль всех предприятий: 11602.0
Предприятия, с прибылью выше среднего значения: a2
Предприятия, с прибылью ниже среднего значения: a1

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     32.0 MiB     32.0 MiB           1   @profile
    28                                         def var1():
    29     32.0 MiB      0.0 MiB           1       num = int(input("Введите количество предприятий для расчета прибыли: "))
    30     32.0 MiB      0.0 MiB           1       ls = []
    31     32.0 MiB      0.0 MiB           1       company = namedtuple('Company', 'name income')
    32     32.0 MiB      0.0 MiB           1       income = 0
    33     32.0 MiB      0.0 MiB           3       for _ in range(num):
    34     32.0 MiB      0.0 MiB           2           ls.append(company(input("Введите название предприятия: "), input("через пробел введите прибыль данного "
    35                                                                                                                  "предприятия за каждый квартал(Всего 4 "
    36                                                                                                                  "квартала): ")))
    37     32.0 MiB      0.0 MiB          22           income = income + sum(int(h) for h in ls[-1].income.split())
    38     32.1 MiB      0.0 MiB           1       print("Размер при использование namedtuple", asizeof.asizeof(ls))
    39     32.1 MiB      0.0 MiB           1       income = float(income) / len(ls)
    40     32.1 MiB      0.0 MiB           1       lsmore = []
    41     32.1 MiB      0.0 MiB           1       lsless = []
    42     32.1 MiB      0.0 MiB           1       print("Средняя годовая прибыль всех предприятий:", income)
    43     32.1 MiB      0.0 MiB           3       for i in ls:
    44     32.1 MiB      0.0 MiB          22           s = sum(int(h) for h in i.income.split())
    45     32.1 MiB      0.0 MiB           2           if s > income:
    46     32.1 MiB      0.0 MiB           1               lsmore.append(i)
    47     32.1 MiB      0.0 MiB           1           elif s < income:
    48     32.1 MiB      0.0 MiB           1               lsless.append(i)
    49                                         
    50     32.1 MiB      0.0 MiB           4       print(f"Предприятия, с прибылью выше среднего значения: {', '.join([l.name for l in lsmore])}")
    51     32.1 MiB      0.0 MiB           4       print(f"Предприятия, с прибылью ниже среднего значения: {', '.join([l.name for l in lsless])}")


memory_usage: 0.55078125
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: a1
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 1234 1234 1234 1234
Введите название предприятия: a2
через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): 4567 4567 4567 4567
Размер при использование recordclass 832
Средняя годовая прибыль всех предприятий: 11602.0
Предприятия, с прибылью выше среднего значения: a2
Предприятия, с прибылью ниже среднего значения: a1

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     32.1 MiB     32.1 MiB           1   @profile
    55                                         def var2():
    56     32.1 MiB      0.0 MiB           1       num = int(input("Введите количество предприятий для расчета прибыли: "))
    57     32.1 MiB      0.0 MiB           1       ls = []
    58     32.1 MiB      0.0 MiB           1       company = recordclass('Company', 'name income')
    59     32.1 MiB      0.0 MiB           1       income = 0
    60     32.1 MiB      0.0 MiB           3       for _ in range(num):
    61     32.1 MiB      0.0 MiB           2           ls.append(company(input("Введите название предприятия: "), input("через пробел введите прибыль данного "
    62                                                                                                                  "предприятия за каждый квартал(Всего 4 "
    63                                                                                                                  "квартала): ")))
    64     32.1 MiB      0.0 MiB          22           income = income + sum(int(h) for h in ls[-1].income.split())
    65     32.1 MiB      0.0 MiB           1       print("Размер при использование recordclass", asizeof.asizeof(ls))
    66     32.1 MiB      0.0 MiB           1       income = float(income) / len(ls)
    67     32.1 MiB      0.0 MiB           1       lsmore = []
    68     32.1 MiB      0.0 MiB           1       lsless = []
    69     32.1 MiB      0.0 MiB           1       print("Средняя годовая прибыль всех предприятий:", income)
    70     32.1 MiB      0.0 MiB           3       for i in ls:
    71     32.1 MiB      0.0 MiB          22           s = sum(int(h) for h in i.income.split())
    72     32.1 MiB      0.0 MiB           2           if s > income:
    73     32.1 MiB      0.0 MiB           1               lsmore.append(i)
    74     32.1 MiB      0.0 MiB           1           elif s < income:
    75     32.1 MiB      0.0 MiB           1               lsless.append(i)
    76     32.1 MiB      0.0 MiB           1       del ls
    77     32.1 MiB      0.0 MiB           4       print(f"Предприятия, с прибылью выше среднего значения: {', '.join([l.name for l in lsmore])}")
    78     32.1 MiB      0.0 MiB           1       del lsmore
    79     32.1 MiB      0.0 MiB           4       print(f"Предприятия, с прибылью ниже среднего значения: {', '.join([l.name for l in lsless])}")
    80     32.1 MiB      0.0 MiB           1       del lsless


memory_usage: 0.05078125

Размер памяти занимаемым объектом 'ls' уменьшился благодаря использованию recordclass вместо namedtuple.

"""
