# 7_1_breast_cancer.py
import pandas as pd
import tensorflow.keras as keras
import numpy as np
from sklearn import preprocessing, model_selection

# wdbc.data 파일에 대해서 모델을 구축하고
# 70% 로 학습하고 30 %에 대해 결과


def read_wdbc():
    wdbc = pd.read_csv('data/wdbc.data',
                       header=None,
                       index_col=0)
    print(wdbc)

    diagnose = wdbc.values[:, 0]
    x = wdbc.values[:, 1:]
    print(diagnose.shape, x.shape)
    print(diagnose[:5])

    enc = preprocessing.LabelEncoder()
    y = enc.fit_transform(diagnose)
    print(y[:5])

    return np.float32(x), y.reshape(-1, 1)


x, y = read_wdbc()
print(x.shape, y.shape)

x = preprocessing.scale(x)
data = model_selection.train_test_split(x, y, train_size=0.7)
x_train, x_test, y_train, y_test = data

model = keras.Sequential()
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=keras.optimizers.SGD(0.1),
              loss=keras.losses.binary_crossentropy,
              metrics='acc')

model.fit(x_train, y_train, epochs=50, verbose=1)

print('acc : ', model.evaluate(x_test, y_test))