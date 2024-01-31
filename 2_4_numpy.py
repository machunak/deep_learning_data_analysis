import numpy as np

a = list('abcdefg')
print(a)

print(a[0], a[-1])
print(a[:3])
print(a[3:])
print(a[::2])
print('-' * 30)

b = np.arange(12)
print(b)
print(type(b))
print(b.shape, b.dtype, b.size)

print(b+1)       #vector
print(np.sin(b)) #universal function
print(sum(b))
print('-' * 30)

c = b.reshape(3, 4)
print(c + 1)        #broadcast
print(c + c)        #vector
print(np.sin(c))    #universal

print('-' * 30)

d = b.reshape(3, 4)
d = b.reshape(3, -1)
d = b.reshape(-1, 3)

print(d)

print(d.reshape(12))
print(d.reshape(-1))
print(d.reshape(d.size))

