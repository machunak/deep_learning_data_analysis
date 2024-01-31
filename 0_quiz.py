import random
import json
import requests, re
def f_2(a=0, b=0, c=0):
    print(a, b, c)

f_2()
f_2(1)
f_2(1, 2)
f_2(1, 2, 3)
f_2(c=3, b=2, a=1)


a = [random.randrange(100) for i in range(10)]

print(list(reversed(a)))
print(a[::-1])
print([a[i] for i in range(len(a)-1, -1, -1) ])
n, m = 3, 5
n, m = m, n
print(m, n)

colors = ['red', 'green', 'YELLOW', 'blue']

print(sorted(colors, key=len))

print(sum([str(i).count('8') for i in range(10000)]))

url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)

text = response.content.decode('utf-8')
datas = json.loads(text)
print(text)
for data in datas:
    for value in data.values():
        print(value, end=' ')
    print()

codes = re.findall(r'"code":"([0-9]+)"', text)
values = re.findall(r'"value":"([가-힣]+)"', text)

for c, v in zip(codes, values):
    print(c, v)
