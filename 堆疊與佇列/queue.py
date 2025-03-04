from collections import deque

que: deque[int] = deque()

que.append(1)
que.append(3)
que.append(2)
que.append(5)
que.append(4)

front: int = que[0]

pop: int = que.popleft()

size: int = len(que)

is_empty: bool = len(que) == 0
