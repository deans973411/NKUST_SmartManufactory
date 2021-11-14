#MLP--MNIST
'''
1.Training set
   In general, we should collect data.
   MNIST have 60,000 data, we just have preprocess 'Feature' and 'Label' for model training.

2.Testing-Predict
   After training, we take 10,000(about 20%) data in testing set, which use for predict its loss function
   and we save this model as .HDF5 format file(.h5)

So the process like:
(1)Date Preprocess: Transfer 'Feature' as 784 float 1-dimantion vector, and normalized float number, transfer 'Label' as One-Hot Encoding.
(2)Build MPL Model: Build model which have input layer, hidden layer and output layer.
(3)Training Molde: Training data set Feature and Label.
(4)Predict accuracy: Predict model accuracy with testing set.
(5)Image Test: Use this model predict on a number inage.
'''
import numpy as np
from keras.datasets import mnist 
from keras.utils import np_utils 
#(1)Data Preprocess
(train_feature, train_label),\
(test_feature, test_label) = mnist.load_data()                                          #Loading data
train_feature_vector = train_feature.reshape(len(train_feature), 784).astype('float32') #Feature transfer
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype('float32')
train_feature_normalize = train_feature_vector / 255                                    #Normalized Feature
test_feature_normalize = test_feature_vector / 255
train_label_onehot = np_utils.to_categorical(train_label)                               #Transfer Label as One-Hot Encoding
test_label_onehot = np_utils.to_categorical(test_label)

#Build Sequential Model
from keras.models import Sequential
model = Sequential()

#(2)Build Input/Output Layer
#Use list.add can increase I/O layer
#Dense is neural layer(connect mesh)
from keras.layers import Dense
model.add(Dense(units = 256,                            #Input Layer
                input_dim = 784,
                kernel_initializer = 'normal',          #Use norm.dist for initialization
                activation = 'relu'))
model.add(Dense(units = 10,                              #It mean out put neural units have 10. Do not set input, it will connect previous layer's neural unit
                kernel_initializer = 'normal',          #Use norm.dist for initialization 'Weight' and 'bias'
                activation = 'softmax'))

#(3)Training Model
'''
3-1 setting training method
Training should use 'compile' method defind 'loss function', 
                    'optimizer' and 'metrics' method predict accuracy
'''
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam', metrics = ['accuracy'])

'''
3-2 Training
'Fit' method can be train
model.fit(x=Feature, y=Label, validation_split=predict precentage, epochs=train time, batch size=how many every epoch, verbose=show training process(0=no,1=all,2=easy))
'''
train_histiry = model.fit(x = train_feature_normalize,
                          y = train_label_onehot, validation_split = 0.2,
                          epochs = 10, batch_size = 200, verbose = 2)
#$ loss:use training set get the loss function
#$ acc: use training set get the accuracy
#$ val_loss:use testing data get the loss function
#$ Val_acc: use testing data get the accuracy
