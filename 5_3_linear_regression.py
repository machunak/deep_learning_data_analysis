# 5_3_linear_regression.py

# linear, multiple
# logistic, softmax

import tensorflow.keras as keras

x = [[1],
     [2],
     [3]]
y = [[1],
     [2],
     [3]]

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(1))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.mse)

model.fit(x, y, epochs=5)
print(model.evaluate(x, y))

print(model.predict(x))