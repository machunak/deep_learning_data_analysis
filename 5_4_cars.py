# 5_4_cars.py
import pandas as pd
import tensorflow.keras as keras
import matplotlib.pyplot as plt

def read_csv():
    # cars = pd.read_csv('data/cars.csv')
    # x = cars.values[:, 1:-1]
    # y = cars.values[:, -1:]
    # print(x.shape, y.shape)
    cars = pd.read_csv('data/cars.csv', index_col=0)
    print(cars)

    x = cars.speed.values.reshape(-1, 1)
    y = cars['dist'].values.reshape(-1, 1)
    print(x.shape, y.shape)

    return x, y

x, y = read_csv()

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(1))

model.compile(optimizer=keras.optimizers.SGD(0.0001),
              loss=keras.losses.mse)

model.fit(x, y, epochs=50, verbose=1)
print(model.evaluate(x, y))

print(model.predict(x))

#속도가 30과 50일 때의 제동거리를 구하고
#예측 결과를 그래프

p = model.predict([[0],
                   [30],
                   [50]], verbose=0)

print(p)

p0, p1, p2 = p[0, 0], p[1, 0], p[2, 0]

plt.plot(x, y, 'ro')
#plt.plot([0, 30, 50], [0, p1, p2], 'g')
plt.plot([0, 30, 50], [p0, p1, p2], 'k')
plt.show()