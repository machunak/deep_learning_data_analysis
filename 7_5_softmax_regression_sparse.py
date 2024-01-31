# 7_5_softmax_regression_sparse.py
import tensorflow.keras as keras
import numpy as np
x = [[1, 2], # C
     [2, 1],
     [4, 5], # B
     [5, 4],
     [8, 9],# A
     [9, 8]]
y = [2, 2, 1, 1, 0, 0]

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=100)

p = model.predict(x, verbose=0)

p_arg = np.argmax(p, axis=1)

print(p_arg)

print('acc : ', np.mean(p_arg == y))