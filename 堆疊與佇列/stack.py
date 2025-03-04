stack: list[int] = []

stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)

peek: int = stack[-1]

pop: int = stack.pop()

size: int = len(stack)

is_empty: bool = len(stack) == 0
