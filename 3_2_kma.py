import requests
import re
import csv
def convertLocation():
    url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
    response = requests.get(url)
    text = response.content.decode('utf-8')
#DOTALL: 여러 줄에 걸쳐있을 때 사용(개행문자를 무시)
# .+ : greedy
# .+? : non-greedy
    locations = re.findall(r'<location wl_ver="3">(.+?)</location>',
                       text, re.DOTALL)
    return locations

def convertLocaProvin(locations):
    provinces = []
    for location in locations:
        province = re.findall(r'<province>(.+?)</province>', location)
        provinces.append(province[0])
    return provinces

def convertLocaCity(locations):
    cities = []
    for location in locations:
        city = re.findall(r'<city>(.+?)</city>', location)
        cities.append(city[0])
    return cities

def convertLocaProvinCity(locations):
    provinces_cities = []
    for location in locations:
        province_city = re.findall(r'<province>(.+?)</province>.+<city>(.+?)</city>', location, re.DOTALL)
        provinces_cities.append(province_city[0])
    return provinces_cities

def convertLocaData(locations):
    dataset = []
    for location in locations:
        data = re.findall(r'<data>(.+?)</data>', location, re.DOTALL)
        dataset.append(data)
    print(len(dataset))
    print(len(dataset[0]))
    return dataset

def convertDataset(dataset):
    dataInclude = []
    for data in dataset:
        data1 = []
        for i in range(len(data)):
            datum = re.findall(r'<.+>(.+?)</.+>', data[i])
            for j in range(len(datum)):
                data1.append(datum[j])

        dataInclude.append(data1)
    return dataInclude


locations = convertLocation()
provinces = convertLocaProvin(locations)
cities = convertLocaCity(locations)
provinces_cities = convertLocaProvinCity(locations)
dataset = convertLocaData(locations)
dataInclude = convertDataset(dataset)
#print(len(dataInclude))
#print(len(dataInclude[0]))
#print(dataInclude)
# for city, data in zip(cities, dataInclude):
#     print(city, end='')
#     for datum in data:
#         print(datum, end='')
#     print()

with open('data/kma.csv', 'w', encoding='utf-8') as f:

    for province, city, data in zip(provinces, cities, dataInclude):

        for i in range(len(data)):
            if i % 6 == 0:
                print(province, file=f, end=',')
                print(city, file=f, end=',')
                print(data[i], file=f, end=',')
            elif i % 6 == 5:
                print(data[i], file=f, end='\n')
            else :
                print(data[i], file=f, end=',')


