import random
def f_1(a, b, c):
    print(a, b, c)

f_1(1, 2, 3)
f_1(c=3, b=2, a=1)

def f_2(a=0, b=0, c=0):
    print(a, b, c)

f_2()
f_2(1, 2, 3)
f_2(1, 2)
f_2(1)
f_2(c=3, b=2, a=1)

a = [random.randrange(100) for i in range(10)]
print(a)

print(list(reversed(a)))

print(a[::-1])

n = 3
m = 8
n, m = m, n
print(n, m)

print([i for i in a if i % 2 == 1])

def to_lower(s):
    return s.lower()

colors = ['red', 'green', 'YELLOW', 'blue']
print(sorted(colors))
print(sorted(colors, key=to_lower))
print(sorted(colors, key=len))

print(len([j for i in range(10000) for j in str(i) if j == '8']))
print(sum([str(i).count('8') for i in range(10000)]))
print(str(list(range(10000))).count('8'))