#################################################
# Deque
#################################################
# import collections
from collections import deque


deque_obj = deque()

deque_obj.append(10)


deque_obj = deque()

deque_obj.append(10)
deque_obj.append(20)
deque_obj.append(30)
deque_obj.append(40)

deque_obj.appendleft(200)


print(deque_obj)
print(deque_obj.pop())
print(deque_obj.pop())
print(deque_obj.pop())
print(deque_obj.pop())
print(deque_obj.popleft())
print(deque_obj)



#################################################
# Queue
#################################################

from queue import Queue

q = Queue(maxsize=3)

print(f'Queue Size: {q.qsize()}')
print('empty',q.empty())
print('full', q.full())
q.put('a')
print(q.empty())
print("added first element")
q.put('b')
print("added second element")
q.put('c')
print('full', q.full())
print("added third element")
q.get()
q.put('d')
print("added fourth element")
q.put_nowait('e')

print(f'Queue Size: {q.qsize()}')

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get_nowait())
print(f'Queue Size: {q.qsize()}')
