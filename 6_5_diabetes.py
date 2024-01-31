# 6_5_diabetes.py
import pandas as pd
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection
import numpy as np
# diabetes.csv 파일에 대해 동작하는 모델 만들고
# 70%의 데이터로 학습하고 30%에 대해 정확도를 구하시오
def read_csv():
    diabetes = pd.read_csv('data/diabetes.csv')
    return diabetes.values[:, :-1], diabetes.values[:, -1:]

x, y = read_csv()
# print(x.shape, y.shape)

# x = preprocessing.minmax_scale(x)   # 정규화(normalization)
x = preprocessing.scale(x)          # 표준화(standardization)

# len_x = int(len(x) * 0.7)
# x_train = x[:len_x, :]
# y_train = y[:len_x, :]
# x_test = x[len_x:, :]
# y_test = y[len_x:, :]
data = model_selection.train_test_split(x, y, train_size=0.7)
x_train, x_test, y_train, y_test = data
model = keras.Sequential()  #functional
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=keras.optimizers.Adam(0.001),
              loss=keras.losses.binary_crossentropy,
              metrics=['binary_accuracy'])

model.fit(x_train, y_train, epochs=200, verbose=1,
          validation_data=(x_test, y_test))
print(model.evaluate(x_test, y_test))

p = model.predict(x_test, verbose=0)
print('acc :', np.mean((p > 0.5) == y_test))