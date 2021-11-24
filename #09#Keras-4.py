#MLP--MNIST--Read weight Test with Mnist
'''
We Build Model_A and Model_B, after the file which is Model_A save, loading it and keep training
'''
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils 
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
(train_feature, train_label),\
(test_feature, test_label) = mnist.load_data()                                          
train_feature_vector = train_feature.reshape(len(train_feature), 784).astype('float32') 
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype('float32')
train_feature_normalize = train_feature_vector / 255                                    
test_feature_normalize = test_feature_vector / 255
train_label_onehot = np_utils.to_categorical(train_label)                               
test_label_onehot = np_utils.to_categorical(test_label)
import matplotlib.pyplot as plt
# prediction command
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


#Build a initial model:Model_A
model = Sequential()
model.add(Dense(256, input_dim = 784, name = 'dense_1'))
model.add(Dense(10, name = 'dense_2'))
'''
Build a model structure: dense_1, dense_2
'''

model.summary()
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam', metrics = ['accuracy'])
train_histiry = model.fit(x = train_feature_normalize,
                          y = train_label_onehot, validation_split = 0.2,
                          epochs = 2, batch_size = 200, verbose = 2)

#Save Model Weigths_A
prediction = model.predict(test_feature_normalize)
plot_images_labels(test_feature, test_label, prediction, 0)
'''
Accumulatee weight data as h5
Check weight with 'Netron' can see 2 dense: dense_1 dense_2
'''
model.save_weights("Mnist_mlp_model_weights_1.h5")
model.save("Mnist_mlp_model_A.h5")  
print("Save new Weigths: 'Mnist_mlp_model_weights_1.h5' done!")
print("Save new model: 'Mnist_mlp_model_A.h5' done!")           
del model       #Clear last


#Build a model:Model_B
model = Sequential()
model.add(Dense(256, input_dim = 784, name = 'dense_1'))
model.add(Dense(10, name = 'dense_2'))
#model.add(Dense(5, name = 'new_dense'))
'''
Build a model structure: dense_1, new_denas
this new model just be effected 'dense_1' from old 'dense_1', 'new_dense' unaffected 
it just load dense_1
'''

#Load Model Weigths, and keep training
model.load_weights("Mnist_mlp_model_weights_1.h5", by_name = True) 

model.summary()
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam', metrics = ['accuracy'])
train_histiry = model.fit(x = train_feature_normalize,
                          y = train_label_onehot, validation_split = 0.2,
                          epochs = 2, batch_size = 200, verbose = 2)
                          
#Save Model Weigths_B
prediction = model.predict(test_feature_normalize)
plot_images_labels(test_feature, test_label, prediction, 0)
model.save_weights("Mnist_mlp_model_weights_2.h5")  
model.save("Mnist_mlp_model_B.h5")   
print("Save new Weigths: 'Mnist_mlp_model_weights_2.h5' done!")
print("Save new model: 'Mnist_mlp_model_B.h5' done!")

'''
==Result==
Model_A accuracy: epoch1-9.95% epoch2-10.09%
Model_B accuracy: epoch1-11.61% epoch2-14.31%

it keep training well
'''
