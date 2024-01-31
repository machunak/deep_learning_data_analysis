# 6_6_preprocessing.py
from sklearn import preprocessing
import numpy as np

def encode(cities):
    print(set(cities))
    print(sorted(set(cities)))

    uniques = sorted(set(cities))
    return [uniques.index(c) for c in cities]

def label_encoder(cities):
    enc = preprocessing.LabelEncoder()
    enc.fit(cities)
    
    result = enc.transform(cities)
    print(result)
    print(enc.fit_transform(cities))

    print(enc.classes_)
    print(enc.inverse_transform(result))

    print(enc.classes_[result])
    eye = np.identity(len(enc.classes_), dtype=np.int32)
    print(eye[result])

def label_binarizer(cities):
    bin = preprocessing.LabelBinarizer()
    bin.fit(cities)
    result = bin.transform(cities)
    print(result)
    print(bin.classes_)
    print(bin.inverse_transform(result))
    print("d")
    print([list(i).index(1) for i in result])
    print([np.max(i) for i in result])
    print([np.argmax(i) for i in result])
    print(np.argmax(result))
    print(np.argmax(result, axis=1))

cities = ['bali', 'paris', 'london', 'bali', 'london']
print(encode(cities))
label_encoder(cities)
label_binarizer(cities)