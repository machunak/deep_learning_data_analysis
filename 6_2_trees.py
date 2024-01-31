# 6_2_trees.py
import pandas as pd
import tensorflow.keras as keras
import numpy as np
#trees.csv 파일을 읽어서
# Girth와 Height로 volume을 예측하는 모델을 만드세요
# Girth가 10 이고 Height가 70일 때와 
# Girth가 15 이고 Height가 80일 때의 volume을 구하세요

def read_csv():
    trees = pd.read_csv('data/trees.csv', index_col=0)
    return trees.values[:, :-1], trees.values[:, -1:]

x, y = read_csv()

model = keras.Sequential()  #functional
model.add(keras.layers.Dense(1))

model.compile(optimizer=keras.optimizers.SGD(0.0001),
              loss=keras.losses.mse)

model.fit(x, y, epochs=50, verbose=1)
print(model.evaluate(x, y))

print(model.predict([[10. , 70.],
                    [15. , 80.]]))

