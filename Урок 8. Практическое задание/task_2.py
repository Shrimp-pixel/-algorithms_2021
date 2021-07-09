"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class WrongBranchError(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if self.root < new_node:
            raise WrongBranchError("New_node is greater then root_node when trying to insert left")
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if self.root > new_node:
            raise WrongBranchError("New_node is lesser then root_node when trying to insert right")
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if self.left_child is not None:
            if self.left_child.root > obj:
                raise WrongBranchError("New_root is lesser then left_child_obj when trying to set New_root")
        if self.right_child is not None:
            if self.right_child.root < obj:
                raise WrongBranchError("New_root is greater then right_child_obj when trying to set New_root")
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
try:
    r.insert_left(40)
except WrongBranchError as e:
    print("Error:", e)

try:
    r.insert_right(4)
except WrongBranchError as e:
    print("Error:", e)

try:
    r.insert_left(4)
    r.insert_right(12)
    print(r.get_right_child().root)
    r.set_root_val(16)
    print(r.get_right_child().get_root_val())
except WrongBranchError as e:
    print("Error:", e)

try:
    r.set_root_val(1)
    print(r.get_right_child().get_root_val())
except WrongBranchError as e:
    print("Error:", e)
