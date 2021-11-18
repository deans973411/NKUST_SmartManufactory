#MLP--MNIST--Read model & Test myself image

import numpy as np
from keras.datasets import mnist 
from keras.utils import np_utils

#(1)Preprocess
'''
When you have a huge model, you can train and save as a file.h5 first, and loading with 'load_model'
and you can pass training process next time.
Before you loading model, you should load model structure first.
'''
(train_feature, train_label),\
(test_feature, test_label) = mnist.load_data()                                          #Loading data
train_feature_vector = train_feature.reshape(len(train_feature), 784).astype('float32') #Feature transfer
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype('float32')
train_feature_normalize = train_feature_vector / 255                                    #Normalized Feature
test_feature_normalize = test_feature_vector / 255
train_label_onehot = np_utils.to_categorical(train_label)                               #Transfer Label as One-Hot Encoding
test_label_onehot = np_utils.to_categorical(test_label)
#(1-1) Load Model and Model Structure
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
load_model('Mnist_mlp_model.h5')
model = Sequential()
model.add(Dense(units = 256,                            #Input Layer
                input_dim = 784,
                kernel_initializer = 'normal',          #Use norm.dist for initialization
                activation = 'relu'))
model.add(Dense(units = 10,                              #It mean out put neural units have 10. Do not set input, it will connect previous layer's neural unit
                kernel_initializer = 'normal',          #Use norm.dist for initialization 'Weight' and 'bias'
                activation = 'softmax'))
#(2)Image Test
'''
We defind a prediction function name 'plot_image_label', module by matplotlib.
We import this plugin first, and defind this function in image size, image number, umage type
, argument, and verify image with its label.

"It copy from last file"
'''

import matplotlib.pyplot as plt                                     #Matplotlib is a data image& vision plugin
def plot_images_labels(images,labels,prediction,start_id,num=10):   #Defind a command for show verify result, show image num as '10'
    fig=plt.gcf()
    fig.set_size_inches(12,14)                                      #Setting image size
    if num>25:                                                      #Max image number at 25
        num=25
    for i in range(0,num):                                          #This loop process for 'show image' and 'show verify label' until num(we set 10)
        ax=plt.subplot(5,5,1+i)                                     #All image distribution as 5 * 5
        ax.imshow(images[start_id], cmap='binary')                  #Color on image as Gray
        if len(prediction) > 0:
            title = 'label = ' + str(labels[i])                  #Show this image verify label
        ax.set_title(title,fontsize=12)
        ax.set_xticks([])                                           #For this window X-axis no scale
        ax.set_yticks([])                                           #For this window Y-axis no scale
        start_id += 1                                               #Counter plus 1
    plt.show()                                                  #After process, show it
prediction = model.predict(test_feature_normalize)
plot_images_labels(test_feature, test_label, prediction, 0)         #input argument and run this function

#$ If it show test image, you done.

#(3)Test Myself Image
'''
We drawing some number image on Microsoft Paint, test this model
reading image data with opencv

Notice:Needing images at less 10, all of the image file format with: <realnumber_datanumber.jpg>
like: 1_2.jpg is draw number1 data2 file 
'''
import glob
import cv2

files = glob.glob("Kera3need_imagedata\*.jpg")
my_feature = []
my_label = []
for file in files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                     #Transfer image color to GRAY
    _,  img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)   #Reverse black and white(because I draw on Microsoft Paint output background array number is black)
    '''
    Here is very important on '_,' , you can run reshape without this char I don't know why
    You can change (200,255) (thresholdValue,maxVal), you should dynamic change thresholdValue on data image
    '''
    my_feature.append(img)                                          #Add this image to list end
    label = file[20]                                                #label is 'Kera3need_imagedata\1.jpg' number 11 char(because of 0~20=no.1~no.21)
    my_label.append(int(label))                                     #Add this label to list end

#process myself image array
my_feature = np.array(my_feature)
my_label = np.array(my_label)
my_feature_vector = my_feature.reshape(len(my_feature), 784).astype('float32')
my_feature_normalize = my_feature_vector / 255
#We import model and model structure just now, so skipping

prediction = model.predict(my_feature_normalize)
plot_images_labels(my_feature, my_label, prediction, 0)  
#$ It will show your image data on screen
