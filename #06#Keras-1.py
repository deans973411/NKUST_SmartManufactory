#06#Keras-1.py
#Class:MDE4-3 Name:Dean Lin
#Keras' Hello World--MNIST

import numpy as np
import pandas as pd
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
