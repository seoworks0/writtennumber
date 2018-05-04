import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np
from keras.models import load_model

model = load_model('mnist/tuyoi.h5')

def predict_strong(a):
    result = model.predict(a)
    print(result)
    return np.argmax(result[0])

#a = np.random.rand(784)
#a = np.array([a])
#predict(a)
