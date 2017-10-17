#! usr/bin/env python
from hyperas.distributions import uniform
from hyperopt import Trials, STATUS_OK, tpe
from keras.datasets import mnist
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Conv2D,MaxPooling2D, Flatten
from keras.models import Sequential
from keras.utils import np_utils
from keras import backend as K
import keras as keras
from hyperas import optim
from hyperas.distributions import choice, uniform, conditional
from keras.optimizers import SGD

def data():
    """Generate the data from mnist"""
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    from keras import backend as K



    img_rows, img_cols = 28, 28

    if K.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
        x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    return x_train, y_train, x_test, y_test


def model_(x_train, y_train, x_test, y_test):
    """
    Model providing function:

    Create Keras model with double curly brackets dropped-in as needed.
    Return value has to be a valid python dictionary with two customary keys:
        - loss: Specify a numeric evaluation metric to be minimized
        - status: Just use STATUS_OK and see hyperopt documentation if not feasible
    The last one is optional, though recommended, namely:
        - model: specify the model just created so that we can later use it again.
    """

    model = Sequential()

    model.add(Conv2D(32,
                     kernel_size=(3, 3),
                     activation='relu',
                     input_shape=input_shape))
    model.add(Conv2D(64,
                     kernel_size=(3, 3),
                     activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense({{choice([200,300,400])}}, activation='relu'))

    model.add(Dense(10, activation='softmax'))



    batch_size = 128
    epochs = 1

    model.compile(optimizer=SGD(lr={{choice([.009,.01,.05,.07])}},decay=1e-6,
                                momentum={{choice([1.2,.6,.9,1.5,1,8])}},
                                nesterov=True),
                      loss=keras.losses.sparse_categorical_crossentropy,
                      metrics=['accuracy'])

    model.fit(x_train,
                y_train,
                batch_size={{choice([16,32,64])}},
                epochs=1,
                verbose=True,
                validation_split=.1)

    score, acc = model.evaluate(x_test, y_test, verbose=0)


    print('Test accuracy:', acc)
    return {'loss': -acc, 'status': STATUS_OK, 'model': model}


if __name__ == "__main__":
    x_train, y_train, x_test, y_test = data()
    best_run, best_model = optim.minimize(model=model_,
                                              data=data,
                                              algo=tpe.suggest,
                                              max_evals=2,
                                              trials=Trials())

    print("Evalutation of best performing model:")
    print(best_model.evaluate(x_test, y_test))
    print("Best performing model chosen hyper-parameters:")
    print(best_run)
