# 7_4_iris_onehot.py
import pandas as pd
import tensorflow.keras as keras
import numpy as np
from sklearn import preprocessing, model_selection
from sklearn.utils import shuffle

# iris_onehot.csv 파일에 대해 모델을 구축
# 70%로 학습 30%에 대해 정확도
# (train_test_split 사용 x)

def read_iris():
    iris = pd.read_csv('data/iris_onehot.csv')
    # iris = shuffle(iris)
    return iris.values[:, :-3], iris.values[:, -3:]


x, y = read_iris()
print(x.shape,y.shape)
x = preprocessing.scale(x)

indices = np.arange(len(x))
np.random.shuffle(indices)
x = x[indices]
y = y[indices]

len_x = int(len(x) * 0.7)
x_train = x[:len_x, :]
y_train = y[:len_x, :]
x_test = x[len_x:, :]
y_test = y[len_x:, :]

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.categorical_crossentropy,
              metrics='acc')

model.fit(x_train, y_train, epochs=200,
          validation_data=(x_test, y_test))

print('acc : ', model.evaluate(x_test, y_test))
