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
        model.add(Dense(units=self.Y[0].shape[0]))
        model.add(Activation('softmax'))
        self.model = model

class MLPTrainer(Trainer):
    """Multi-Layer Perceptron Classifier"""

    def build_model(self):
        from keras.models import Sequential
        from keras.layers import Flatten, Dense, Activation

        model = Sequential()
        model.add(Flatten(input_shape=self.X[0].shape))
        model.add(Dense(units=32, activation='relu'))
        model.add(Dense(units=self.Y[0].shape[0]))
        model.add(Activation('softmax'))
        self.model = model
class CNNTrainer(Trainer):
    """Convolutional Neural Network Classifier"""

    def build_model(self):
        from keras.models import Sequential
        from keras.layers import Conv2D, Dense, MaxPooling2D, Dropout, Flatten

        model = Sequential()
        model.add(Conv2D(36, kernel_size=2, strides=1, activation='relu', input_shape=self.X[0].shape))
        model.add(MaxPooling2D(2))
        model.add(Flatten())
        model.add(Dense(100, activation='relu'))
        model.add(Dense(self.Y[0].shape[0], activation='softmax'))
        
        self.model = model
