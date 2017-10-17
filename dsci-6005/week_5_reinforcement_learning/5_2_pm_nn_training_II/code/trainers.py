# define different architectures for experimentation in this file

from trainer import Trainer
from keras.regularizers import l2


class MLRTrainer(Trainer):
    """Multi-Class Logistic Regression Classifier"""

    def build_model(self):
        from keras.models import Sequential
        from keras.layers import Flatten, Dense, Activation

        model = Sequential()
        model.add(Flatten(input_shape=self.X[0].shape))
        model.add(Dense(units=self.Y[0].shape[0], W_regularizer=l2(self.C['reg'])))
        model.add(Activation('softmax'))
        self.model = model

class MLPTrainer(Trainer):
    """Multi-Layer Perceptron Classifier"""

    def build_model(self):
        from keras.models import Sequential
        from keras.layers import Flatten, Dense, Activation

        model = Sequential()
        model.add(Flatten(input_shape=self.X[0].shape))
        model.add(Dense(units=self.C['hidden_size'], activation='relu'))
        model.add(Dense(units=self.Y[0].shape[0]))
        model.add(Activation('softmax'))
        self.model = model

class CNNTrainer(Trainer):
    """CNN Trainer"""
    
    def build_model(self):
        from keras.layers import Conv2D, Dropout, Flatten, Dense, MaxPooling2D, Activation
        from keras.models import Sequential
        
        model =Sequential()
        model.add(Conv2D(32, (2,2), input_shape=self.X[0].shape, activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Conv2D(64, (2,2), activation='relu'))  
        model.add(Dropout(.3))
        model.add(Flatten())                   
        model.add(Dense(units=self.Y[0].shape[0]))
        model.add(Activation('softmax'))
        self.model = model
        
    
