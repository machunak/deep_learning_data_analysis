# 8_5_adult.py
import pandas as pd
import numpy as np
import tensorflow.keras as keras
from sklearn import preprocessing, model_selection 

def read_adult():
    adult = pd.read_csv('data/adult.data',
                       header=None)
    print(adult)
    x = [
        adult[0].values,
        adult[2].values,
        adult[4].values,
        adult[10].values,
        adult[11].values,
        adult[12].values,
    ]
    x = np.float32(x).transpose()
    print(x.shape)
    enc = preprocessing.LabelBinarizer()
    y = enc.fit_transform(adult[14])
    print(y)

    work = enc.fit_transform(adult[1])
    edu = enc.fit_transform(adult[3])
    marital = enc.fit_transform(adult[5])
    occu =  enc.fit_transform(adult[6])
    rel =  enc.fit_transform(adult[7])
    race = enc.fit_transform(adult[8])
    sex =  enc.fit_transform(adult[9])
    country = enc.fit_transform(adult[13])
    x = np.hstack([x, work, edu, marital, occu, rel, race, sex, country])
    return x, y


x, y = read_adult()

x = preprocessing.scale(x)

data = model_selection.train_test_split(x, y, train_size=0.7)
x_train, x_test, y_train, y_test = data
model = keras.Sequential()  #functional
model.add(keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=keras.optimizers.SGD(0.01),
              loss=keras.losses.binary_crossentropy,
              metrics=['binary_accuracy'])

model.fit(x_train, y_train, epochs=200, verbose=1,
          validation_data=(x_test, y_test))