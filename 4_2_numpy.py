import numpy as np

a = np.arange(12).reshape(3, 4)
print(a[-1, -1])    # fancy indexing

print(a[:, -1])

print(a[-1:, :])
print(a[:, -1:])

print('-' * 30)
print(np.zeros(3))
print(np.zeros(3, dtype=np.int32))
print(np.zeros((3, 4)))
print(np.ones((3, 4)))

print(np.full((3, 4), fill_value=-1))
print('-' * 30)

b = np.zeros((5, 5), dtype=np.int32)
b[[0, -1]] = 1
b[:, [0, -1]] = 1
b[1:4, 1:4] = 2

b[range(5), range(5)] = 3

print(b)

print('-' * 30)

c1 = np.arange(12).reshape(3, 4)
c2 = np.arange(12).reshape(4, 3)

print(np.dot(c1, c2))

print(c1)
print(np.transpose(c1))