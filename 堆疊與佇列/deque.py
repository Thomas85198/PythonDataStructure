from collections import deque
deq: deque[int] = deque()

deq.append(2)
deq.append(5)
deq.append(4)
deq.appendleft(3)
deq.appendleft(1)

front: int = deq[0]
rear: int = deq[-1]

pop_front: int = deq.popleft()
pop_rear: int = deq.pop()

size: int = len(deq)

is_empty: bool = len(deq) == 0
