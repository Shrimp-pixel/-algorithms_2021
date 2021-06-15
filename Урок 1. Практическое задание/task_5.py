"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class StackClass:
    allStack = []

    def __init__(self):
        self.elems = []
        self.nextstack = None
        StackClass.allStack.append(self)

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        if len(self.elems) < 10:
            self.elems.insert(0, el)
        else:
            if self.nextstack is None:
                self.nextstack = StackClass()
            self.nextstack.push_in(el)

    def pop_out(self):
        return self.elems.pop(0)

    def get_val(self):
        return self.elems[0]

    def stack_size(self):
        return len(self.elems)


sc = StackClass()
for i in range(101):
    sc.push_in("Тарелка№ " + str(i))

for i in StackClass.allStack:
    print(i.elems)

print()
StackClass.allStack.clear()
sc = StackClass()
for i in range(11):
    sc.push_in("Тарелка№ " + str(i))

sc = StackClass()
for i in range(12, 32):
    sc.push_in("Тарелка№ " + str(i))

for i in StackClass.allStack:
    print(i.elems)

