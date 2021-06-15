"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

data_base = {"Company1": 100, "Company2": 29694, "Company3": 20, "Company4": 240, "Company5": 45678, "Company6": 3569,
             "Company7": 99, "Company8": 12345}


def fun1(db):  # 0(N^2)
    income = list(db.values())  # 0(N)
    names = list(db.keys())  # 0(N)
    max_income = [income[0], income[1], income[2]]  # 0(1)
    max_comp = [names[0], names[1], names[2]]  # 0(1)
    income = income[3:]  # 0(N)
    names = names[3:]  # 0(N)
    for i in income:  # 0(N)
        mininmax = min(max_income)  # O(N)
        if i > mininmax:  # O(1)
            max_comp.pop(max_income.index(mininmax))  # 0(1)
            max_income.pop(max_income.index(mininmax))  # 0(1)
            max_comp.append(names[income.index(i)])  # 0(1)
            max_income.append(i)  # 0(1)

    return dict(zip(max_comp, max_income))  # 0(1)


def fun2(db):  # 0(N^3)
    income = list(db.values())  # 0(N)
    names = list(db.keys())  # 0(N)
    while len(income) > 3:  # 0(N)
        for i in income:  # 0(N)
            for j in income:  # 0(N)
                if j < i:  # 0(1)
                    break  # 0(1)
            else:
                names.pop(income.index(i))  # 0(1)
                income.pop(income.index(i))  # 0(1)
    return dict(zip(names, income))  # 0(1)


print(fun1(data_base))
print(fun2(data_base))

""" Второе решение оказалось хуже т.к. используется 3 цикла вместо функции min и одного цикла как в превом решении"""
