import csv


def read_us500_1():

    arr_2d = []
    arr_1d = []

    with open('data/us-500.csv', 'r', encoding='utf-8') as f:

        for idx, line in enumerate(f):
            if idx != 0:
                arr_1d.append(list(eval(line)))
            # for idx, arr in enumerate(arr_1d):
            #
            #     arr_1d[idx] = arr_1d[idx].strip('\n')
            #     arr_1d[idx] = arr_1d[idx].strip('"')

        arr_2d.append(arr_1d)
    return arr_2d


def read_us500_2():
    #arr_2d = []
    arr_1d = []

    with open('data/us-500.csv', 'r', encoding='utf-8') as f:
        f.readline()
        for item in csv.reader(f):
            arr_1d.append(item)

    return arr_1d

rows = read_us500_2()
print(*rows[:3], sep='\n')