# kma.csv 파일을 2차원 리스트로 반환하는 함수를 만드세요
import csv
import sqlite3

def read_kma():
    with open('data/kma.csv', 'r', encoding='utf-8') as f:
        return [line for line in csv.reader(f)]

def create_db():
    conn =  sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    query = 'CREATE TABLE kma (prov TEXT, city TEXT, mode TEXT, tmEf TEXT, wf TEXT, tmn TEXT, tmx TEXT, rnSt TEXT)'
    conn.execute(query)

    conn.commit()
    conn.close()

def insert_row(row):
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    query = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'.format(*row)
    conn.execute(query)

    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()
    rows = []
    query = 'SELECT * FROM kma'
    for r in conn.execute(query):
        rows.append(r)

    #conn.commit()
    conn.close()
    return rows

def insert_all(rows):
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()

    base = 'INSERT INTO kma VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}")'
    for r in rows:
        base = base.format(*r)
        conn.execute(base)

    conn.commit()
    conn.close()

def search_city(city):
    conn = sqlite3.connect('data/kma.sqlite3')
    cursor = conn.cursor()
    rows = []
    query = 'SELECT * FROM kma WHERE city="{}"'.format(city)
    for r in conn.execute(query):
        rows.append(r)
    conn.close()
    return rows

# rows = read_kma()
# for row in rows:
#    insert_row(row)


row = search_city("이천")
print(row)
#print(*rows, sep='\n')
#create_db()
#print(*rows, sep='\n')

#print(rows)

#     insert_row(row)

#
# conn =  sqlite3.connect('data/kma.sqlite3')
# cursor = conn.cursor()
#
# query = 'DELETE FROM kma'
# conn.execute(query)
#
# conn.commit()
# conn.close()