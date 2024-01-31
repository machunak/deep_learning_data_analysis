# 6_1_multiple_regression.py

import tensorflow.keras as keras

x = [[1, 2],
     [2, 1],
     [4, 5],
     [5, 4],
     [8, 9],
     [9, 8]]
y = [[3],
     [3],
     [9],
     [9],
     [17],
     [17]]

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(1))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.mse)

model.fit(x, y, epochs=100)
print(model.evaluate(x, y))

print(model.predict([[2, 7],
                    [5, 1]]))