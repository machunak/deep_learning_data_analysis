# 7_6_iris_sparse.py
import pandas as pd
import tensorflow.keras as keras
import numpy as np
from sklearn import preprocessing, model_selection
# iris.csv 파일에 대해서 sparse 버전의 모델을 생성
np.set_printoptions(linewidth=1000)

def read_iris():
    iris = pd.read_csv('data/iris.csv')

    enc = preprocessing.LabelEncoder()
    y = enc.fit_transform(iris.values[:, -1]) # 1차원
    x = iris.values[:, :-1]
    return np.float32(x), y, enc.classes_


x, y, classes = read_iris()
print(x.shape,y.shape)
x = preprocessing.scale(x)

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(3, activation='softmax'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.sparse_categorical_crossentropy,
              metrics='acc')

model.fit(x, y, epochs=200,
          validation_data=(x, y))

p = model.predict(x, verbose=0)
p = np.argmax(p, axis=1)

print(p)
print(y)

bools = (p != y)
wrong = x[bools]
print(wrong)

y_wrong, p_wrong = y[bools], p[bools]
print(y_wrong)
print(p_wrong)

print(classes[y_wrong])
print(classes[p_wrong])

for dd, pp, yy in zip(wrong, classes[p_wrong], classes[y_wrong]):
    print(dd, pp, yy)