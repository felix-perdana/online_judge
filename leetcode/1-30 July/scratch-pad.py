from collections import deque
d = deque([(1, 2)])

print(d)
item = d.popleft()
print(d)
print(item)
