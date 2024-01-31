# 6_7_boston.py
import pandas as pd
import tensorflow.keras as keras
import numpy as np
from sklearn import preprocessing, model_selection
# boston.xls 파일에 대해 모델을 구축하고
# 70% 로 학습하고 30%에 대해 결과를 보여준다
# (예측 결과가 정답하고 가격이 얼마 차이나는지 보여준다)

def read_boston():
    boston = pd.read_excel('data/boston.xls')
    return boston.values[:, :-2], boston.values[:, -2:-1]


x, y = read_boston()

x = preprocessing.scale(x)
data = model_selection.train_test_split(x, y, train_size=0.7)
x_train, x_test, y_train, y_test = data

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(1))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.mse,
              metrics='mae')

model.fit(x_train, y_train, epochs=200, verbose=1)
print('mae : ', model.evaluate(x_test, y_test))

p = model.predict(x_test, verbose=0)
print('mae : ', np.mean(np.abs(p - y_test)))

