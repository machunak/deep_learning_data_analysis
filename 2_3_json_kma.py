import requests
import json
import re

#url = 'https://www.naver.com/'
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)
print(response)
print(response.text)
print(response.content)

text = response.content.decode('utf-8')
print(text)

results = json.loads(text)
for result in results:
    for value in result.values():
        print(value, end=' ')
    print()

print('-' * 30)

numbers = re.findall(r'[0-9]+', text)
regions = re.findall(r'[가-힣]+', text)

codes = re.findall(r'"code":"([0-9]+)","value":"([가-힣]+)"', text)

print(codes)
#print(values)
for c, v in codes:
    print(f'{c} {v}')
