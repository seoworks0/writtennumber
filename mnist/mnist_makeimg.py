import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt
import numpy as np

batch_size = 128
num_classes = 10
epochs = 1

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784) # 2次元配列を1次元に変換
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')   # int型をfloat32型に変換
x_test = x_test.astype('float32')
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

for i in range(0,200):
    a = np.argmax(y_train[i])
    fp = 'img/' + str(a) + '_' + str(i) + '.png'
    f = x_train[i]
    random = f.reshape(28,28)
    plt.imshow(random, cmap = 'gray', vmin = 0, vmax = 255, interpolation = 'none')
    plt.savefig(fp)
