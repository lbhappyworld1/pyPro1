import numpy as np
from keras.datasets import mnist

from keras.models import Sequential

from keras.layers import Dense,Dropout,Flatten

from keras.layers import Conv2D,MaxPooling2D

#os.chdir("/sdcard/qpython/tmp")

#model_dir="/tmp/"

(X_train,Y_train),(X_test,Y_test) = mnist.load_data()

print(X_train[0].shape)

print(Y_train[0])

