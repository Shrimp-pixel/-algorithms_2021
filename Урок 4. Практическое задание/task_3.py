"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = []
    for i in enter_num:
        revers_num.insert(0, i)
    return ''.join(revers_num)


n = 123456789

print(timeit.timeit(
    "revers_1(n)",
    globals=globals(),
    number=100000
))
print(timeit.timeit(
    "revers_2(n)",
    globals=globals(),
    number=100000
))
print(timeit.timeit(
    "revers_3(n)",
    globals=globals(),
    number=100000
))
print(timeit.timeit(
    "revers_4(n)",
    globals=globals(),
    number=100000
))

run('revers_1(n)')
run('revers_2(n)')
run('revers_3(n)')
run('revers_4(n)')

"""
0.2433801
0.13600660000000003
0.03395999999999999
0.10522610000000004
revers_1 - имеет экспоненциальную сложность поэтому скорость выполнения низкая
revers_2 - имеет линейную сложность поэтому скорость выполнения средняя
revers_3 - использует срез и имеет самую быструю скорость выполнения
revers_4 - имеет линейную сложность поэтому скорость выполнения средняя
"""
