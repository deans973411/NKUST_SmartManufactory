#Keras' Hello World--MNIST

import numpy as np
import pandas as pd
#from tensorflow.keras import models
from keras.datasets import mnist                    #run first, download MNIST<mnist.npz> in <.keras\datasets>
(train_feature, train_label), \
(test_feature, test_label) = mnist.load_data()      #after download data, distribation in 4 variable

#PartA-Check training data
'''
The training data composition with image(number and graph) and labels(number and trurh value)
And every image composition in 28 * 28 pixel, lables composition from 0 ~ 9 number
'''
print(len(train_feature),len(train_label))          #Show training data length with len()
#$ 60000 60000
print(train_feature.shape, train_label.shape)       #Show training data dimension with .shape
#$ (60000, 28, 28) (60000,)

#PartB-Preprocess the data
#B-1 Show training data image and value
import matplotlib.pyplot as plt
plt.figure()                        #make a figure
#figure: The top level container for all the plot elements
plt.imshow(train_feature[50000])    #show training image, image number in []
plt.colorbar()                      #show color bar right hend site
plt.grid(False)                     #Show the mesh or not
plt.show()          #show this image

#PartC-Feature Preproces
train_feature_vector = train_feature.reshape(len(train_feature),784).astype('float32')
test_feature_vector = test_feature.reshape(len(test_feature),784).astype('float32')
'''
Use reshape() function transfer 28*28 image to 784*1 1 dimension vector
Use astype() functiom transfer every number to float format
'''

print(train_feature_vector.shape, test_feature_vector.shape)    #show properties with .shape
#$(60000, 784) (10000, 784)

print(train_feature_vector[50000])
#show no.1 image data, the data which show with from 0 to 255 float is pixel inside this image

#PartD-Image Normalize
train_feature_normalize = train_feature_vector/255
test_feature_normlize = test_feature_vector/255
#the number from 0 to 255 normalize by division 255 this method make result precise
print(train_feature_normalize[50000])#show the first image data after normalize
#The data have be 0~1 float

#PartE-Label data Preproces
'''
Label is 0~9 number. To Increase efficiency, neural output code with 'One-Hot Encoding'
Just only a number is 1, other are 0
Use 'np_utils.to_categorical can transfer One-Hot Encoding code'
'''
from keras.utils import np_utils #import One-Hot Encoding mod

train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)
print(train_label_onehot[0:5])      #Check Label after One-Hot Encoding code
