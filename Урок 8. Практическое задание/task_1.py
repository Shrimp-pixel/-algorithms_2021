"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import Counter


def haffman_tree(s):
    elem_frequency = list(sorted(Counter(s).items(), key=lambda item: item[1]))
    if len(elem_frequency) != 1:
        while len(elem_frequency) > 1:
            weight = elem_frequency[0][1] + elem_frequency[1][1]
            comb = {0: elem_frequency.pop(0)[0],
                    1: elem_frequency.pop(0)[0]}

            for j, _count in enumerate(elem_frequency):
                if weight > _count[1]:
                    continue
                else:
                    elem_frequency.insert(j, (comb, weight))
                    break
            else:
                elem_frequency.append((comb, weight))

    else:
        weight = elem_frequency[0][1]
        comb = {0: elem_frequency.pop(0)[0], 1: None}
        elem_frequency.append((comb, weight))
    return elem_frequency[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "beep boop beer!"

haffman_code(haffman_tree(s))
for i in s:
    print(code_table[i], end=' ')
print()
