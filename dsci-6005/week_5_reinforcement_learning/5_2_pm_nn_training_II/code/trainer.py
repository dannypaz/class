import numpy as np


class Trainer:
    """Class for loading data and defining, compiling, and fitting a model"""

    def __init__(self, config):
        self.C = config # save sacred config dict

    def load_data(self):
        from keras.datasets import mnist
        from keras.utils.np_utils import to_categorical
        [X, y], _ = mnist.load_data()
        self.X = np.expand_dims(X, axis=-1).astype(np.float) / 255.
        self.Y = to_categorical(y)

    def build_model(self):
        err_str = 'You must implement this method in a subclass defined in trainers.py!'
        raise NotImplementedError(err_str)

    def compile_model(self):
        self.model.compile(optimizer='adam', loss=self.C['loss'], metrics=['accuracy'])
        self.model.summary()

    def fit(self):
        from keras.callbacks import TensorBoard
        from callbacks import AddTimestamp
        self.model.fit(self.X, self.Y,
                       epochs=self.C['epochs'],
                       validation_split=.1,
                       callbacks=[AddTimestamp(self.C), TensorBoard(histogram_freq=1)])
