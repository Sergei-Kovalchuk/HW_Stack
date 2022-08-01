class Stack:
  stack = []
  def isEmpty(self):
    return not bool(self.stack)
  def push(self, elem):
    self.stack.append(elem)
  def pop(self):
    return self.stack.pop()
  def peek(self):
    return self.stack[-1]
  def size(self):
    return len(self.stack)

def check_brasckets(str):
  stack = Stack()
  pairs_elems = {"{" : "}",
                 "[" : "]",
                 "(" : ")"}
  available_elems = list(pairs_elems.keys()) + list(pairs_elems.values())
  elem_list = list(filter(lambda elem: elem in available_elems, str))
  if not elem_list:
    return "Пусто"
  if len(elem_list) % 2 == 0:
    for elem in elem_list:
      if not stack.isEmpty() and pairs_elems.get(stack.peek(), False) == elem:
        stack.pop()
      else:
        stack.push(elem)
    if stack.isEmpty():
      return "Сбалансировано"
  return "Несбалансировано"


if __name__ == '__main__':
  print('(((([{}]))))', check_brasckets('(((([{}]))))'))
  print('[([])((([[[]]])))]{()}', check_brasckets('(((([{}]))))'))
  print('{{[()]}}', check_brasckets('{{[()]}}'))
  print('}{}', check_brasckets('}{}'))
  print('{{[(])]}}', check_brasckets('{{[(])]}}'))
  print('[[{())}]', check_brasckets('[[{())}]'))

