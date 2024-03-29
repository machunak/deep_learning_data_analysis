# 8_2_multi_layers.py
import tensorflow.keras as keras
from sklearn import preprocessing

mnist = keras.datasets.mnist.load_data()
print(len(mnist))
print(len(mnist[0]))

(x_train, y_train), (x_test, y_test) = mnist
print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)
print(y_test)
print(set(y_train.reshape(-1)))

# scaler = preprocessing.MinMaxScaler()
# scaler.fit(x_train)

# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)

x_train = x_train / 255
x_test = x_test / 255

model = keras.Sequential([
    keras.layers.Input(shape=[784]),
    # (?, 512) = (?, 784) @ (784, 512) + 512
    keras.layers.Dense(512, activation='relu'),
    # (?, 256) = (?, 512) @ (512, 256) + 256
    keras.layers.Dense(256, activation='relu'),
    # (?, 256) = (?, 256) @ (256, 256) + 256
    keras.layers.Dense(256, activation='relu'),
    # (?, 128) = (?, 256) @ (256, 128) + 128
    keras.layers.Dense(128, activation='relu'),
    # (?, 10) = (?, 128) @ (128, 10) + 10
    keras.layers.Dense(10, activation='softmax'),
])
model.summary()
exit()

model.add(keras.layers.Dense(512, activation='relu'))
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer=keras.optimizers.RMSprop(0.001),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

model.fit(x_train, y_train, epochs=10, verbose=1,
          validation_data=(x_test, y_test),
          batch_size=32)
