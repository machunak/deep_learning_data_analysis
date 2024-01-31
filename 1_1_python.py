#1_1_python.py

#0 123 4

for i in range(0, 5):
    for j in range(0, 5):
        if i == j or i == 4 - j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()
for i in range(0, 5):
    for j in range(0, 5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print('*', end='')
        else:
            print(' ', end='')
    print()