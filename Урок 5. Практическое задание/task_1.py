"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple

num = int(input("Введите количество предприятий для расчета прибыли: "))
ls = []
company = namedtuple('Company', 'name income')
income = 0
for _ in range(num):
    ls.append(company(input("Введите название предприятия: "), input("через пробел введите прибыль данного "
                                                                     "предприятия за каждый квартал(Всего 4 "
                                                                     "квартала): ")))
    income = income + sum(int(h) for h in ls[-1].income.split())

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
