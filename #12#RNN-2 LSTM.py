#RNN-MNIST
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils

#Proprocess
(train_feature, train_label),\
(test_feature, test_label) = mnist.load_data()
train_feature_vector = train_feature.reshape(len(train_feature),28,28).astype('float32')
test_feature_vector = test_feature.reshape(len(test_feature),28,28).astype('float32')
train_feature_normalize = train_feature_vector/255
test_feature_normalize = test_feature_vector/255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

#Build recurrent nuarl network
from keras.models import Sequential
from keras.layers import  Dropout, Dense
from keras.layers.recurrent import LSTM
'''
RNN-LSTM base on RNN creurrent, and strengthen its memory capacity with forget gate, input gate, memory cell and output gate.
'''

model = Sequential()
'''
model.add(LSTM(
    input_shape=(Time_steps,Input_size),
    units=Cell_size,
    unroll=Boolean_value
))
'''
model.add(LSTM(input_shape=(28, 28), units=256, unroll=True))
model.add(Dropout(0.1))
model.add(Dense(units=10, kernel_initializer='normal', activation='softmax'))

#Training model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
train_history = model.fit(x=train_feature_normalize, y=train_label_onehot, validation_split=0.2, epochs=10, batch_size=200, verbose=2)

#Predict accuracy
import matplotlib.pyplot as plt
scores = model.evaluate(test_feature_normalize, test_label_onehot)
print('\nAccuracy=',scores[1])
def plot_images_labels(images,labels,prediction,start_id,num=10):
    fig=plt.gcf()
    fig.set_size_inches(12,14)
    if num>25:
        num=25
    for i in range(0,num):
        ax=plt.subplot(5,5,1+i)
        ax.imshow(images[start_id], cmap='binary')
        if len(prediction) > 0:
            title = 'label = ' + str(labels[i])
        ax.set_title(title,fontsize=12)
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    plt.show()
prediction = model.predict(test_feature_normalize)
plot_images_labels(test_feature, test_label, prediction, 0)

#Save model
model.save('Mnist_RNN(LSTM)_Model.h5')
print('saving...done!')
del model