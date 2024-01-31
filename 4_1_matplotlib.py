import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import colormaps

def p4():
    x = [random.randrange(100) for _ in range(100)]
    y = [random.randrange(100) for _ in range(100)]

    plt.subplot2grid(shape=(3, 4), loc=(1, 1), rowspan=2)
    plt.plot(x, y, 'r>')

    plt.subplot2grid(shape=(3, 4), loc=(0, 0), rowspan=3)
    plt.plot(x, y, 'go')

    plt.subplot2grid(shape=(3, 4), loc=(0, 1), colspan=3)
    plt.plot(x, y, 'k')

    plt.subplot2grid(shape=(3, 4), loc=(1, 2), colspan=2, rowspan=2)
    plt.scatter(x, y, s=3)

    plt.show()

def p5():
    males = [30, 35, 27, 31, 37]
    females = [29, 36, 37, 42, 19]

    #idx_m = range(0, len(males)*2, 2)
    #idx_f = range(1, len(females)*2, 2)

    idx = np.arange(len(males))
    plt.bar(idx, males, width=0.45)
    plt.bar(idx+0.5, females, width=0.45)
    plt.show()

def p6():
    #data = []
    with open('data/2016_GDP.txt', 'r', encoding='utf-8') as f:
        data = [line for line in f.readlines()]
        x = []
        y = []
        for i in range(1, 11):
            x.append(data[i].split(':')[1])
            y.append(data[i].split(':')[2])
            y[i-1] = int(y[i-1].replace(',', ''))
        idx = np.arange(len(x))
        plt.rcParams['font.family'] = 'Malgun Gothic'
        plt.rcParams['axes.unicode_minus'] = False
        #for i in range(0, 10):
        plt.bar(idx, y, color=['MediumSeaGreen', 'DarkGreen', 'DarkOliveGreen'])

        #plt.bar(x, y, width=0.45)
        plt.xticks(idx, x, rotation=45)
        plt.subplots_adjust(bottom=0.2, top=0.9)
        plt.title('2016 GDP Top10')
        plt.show()

def p7():
    x = np.arange(100)
    plt.scatter(x, x, s=5, c=x)
    y = [i for i in range(100, 0, -1)]
    plt.scatter(x, y, s=5, c=y)
    plt.show()

def p8():
    v = colormaps.get_cmap('viridis')
    print(v)

    print(v(-1))
    print(v(0))
    print(v(255))
    print(v(256))
p8()
#print(list(colormaps))
