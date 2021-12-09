#CNN-MNIST
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils

#Proporcess
(train_feature, train_label),\
(test_feature, test_label) = mnist.load_data()
train_feature_vector = train_feature.reshape(len(train_feature),
                        28, 28, 1).astype('float32')
test_feature_vector = test_feature.reshape(len(test_feature),
                        28, 28, 1).astype('float32')
train_feature_normalize = train_feature_vector/255
test_feature_normalize = test_feature_vector/255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

#Build convolution neural network
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
'''
Convolution: got feature map from import image
Maxpooling: a method reduce boundary sensitive, control overfitting degree
Dropout: a method control overfitting drgree, according to "rate" turn-off cell connecttion randemly
Flatten: transfer input to 1-dimention, connect to dense
Dense: connected neural cell
'''

model = Sequential()
model.add(Conv2D(filters=10, kernel_size=(3,3), padding='same', input_shape=(28,28,1),activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=20, kernel_size=(3,3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#Training model
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam', metrics = ['accuracy'])
model.history = model.fit(x=train_feature_normalize,
                            y=train_label_onehot, validation_split=0.2,
                            epochs=10, batch_size=200, verbose=1)

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
model.save('Mnist_CNN_Model.h5')
print('saving...done!')
del model