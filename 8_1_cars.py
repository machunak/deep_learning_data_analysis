# 8_1_cars.py
import pandas as pd
import tensorflow.keras as keras
import numpy as np
from sklearn import preprocessing, model_selection
# car.data 파일에 대해 동작하는 모델 생성
# 70% 학습 30% 결과

def read_cars_1():
    car = pd.read_csv('data/car.data',
                      header=None)
    print(car)

    features = []
    enc = preprocessing.LabelEncoder()
    for i in range(6):
        # print(car[i].values)
        # print(car.values[:, i])
        result = enc.fit_transform(car.values[:, i])
        # print(result)
        features.append(result)

    x = np.int32(features)
    print(x.shape)

    x = x.transpose()
    # x = x.T
    print(x.shape)

    y = enc.fit_transform(car.values[:, -1])
    return x, y
def read_cars_2():
    car = pd.read_csv('data/car.data',
                      header=None)

    enc = preprocessing.LabelEncoder()
    features = [enc.fit_transform(car.values[:, i]) for i in range(6)]
  
    return np.int32(features).T, enc.fit_transform(car.values[:, -1])

x, y = read_cars_2()

x = preprocessing.scale(x)
data = model_selection.train_test_split(x, y, train_size=0.7)
x_train, x_test, y_train, y_test = data

model = keras.Sequential()
model.add(keras.layers.Dense(4, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

model.fit(x_train, y_train, epochs=50, verbose=1)

print('acc : ', model.evaluate(x_test, y_test))