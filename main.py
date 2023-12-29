

class Stack:
    def __init__(self):
        self.stack = []
        pass

    def is_empty(self):  # проверка стека на пустоту. Метод возвращает True или False
        return True if self.stack else False

    def push(self, item):  # добавляет новый элемент на вершину стека. Метод ничего не возвращает
        self.stack.append(item)
        pass

    def pop(self):  # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
        removed_item = self.stack.pop()
        return removed_item

    def peek(self):  # возвращает верхний элемент стека, но не удаляет его. Стек не меняется
        if self.is_empty():
            last_element = self.stack[-1]
            return last_element

    def size(self):  # возвращает количество элементов в стеке
        len_stack = len(self.stack)
        return len_stack


a = input()
open_simbols = "([{"
close_simbols = ")]}"
res = Stack()
ans = True
for i in a:
    if i in open_simbols:
        res.push(i)
    elif i in close_simbols:
        if not res.is_empty():
            ans = False
            break
        if res.peek() == '(' and i == ')' or res.peek() == '[' and i == ']' or res.peek() == '{' and i == '}':
            res.pop()
            continue
        ans = False
        break

print('Сбалансировано' if ans else 'Несбалансировано')
