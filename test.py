#test py keras
import numpy as np
import tensorflow
from tensorflow import keras
from keras.datasets import mnist
#from keras.models import Sequential
#from keras.layers import Dense,Dropout,Flatten
#from keras.layers import Conv2D,MaxPooling2D
(X_train,Y_train),(X_test,Y_test) = keras.datasets.mnist.load_data()
print(X_train[0].shape)
print(Y_train[0])

