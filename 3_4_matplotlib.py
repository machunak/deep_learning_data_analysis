import matplotlib.pyplot as plt
import numpy as np

def p1():
    plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'r')   # line
    plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'go')  # scatter
    plt.show()

def p2():
    x = np.arange(-10, 10, 0.1)
    plt.plot(x, x**2, 'r')
    plt.show()


def p3():
    x = np.arange(0.01, 2, 0.01)
    plt.plot(x, np.log(x), 'r')
    plt.plot(x, -np.log(x), 'b')
    plt.plot(-x, np.log(x), 'g')
    plt.plot(-x, -np.log(x), 'y')
    plt.show()

p3()