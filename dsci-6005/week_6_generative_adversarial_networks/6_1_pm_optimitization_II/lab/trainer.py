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
        self.model.compile(optimizer=self.C['optimizer'], loss='categorical_crossentropy', metrics=['accuracy'])
        self.model.summary()

    def fit(self):
        from keras.callbacks import TensorBoard
        from callbacks import AddTimestamp

        cbs = [AddTimestamp(self.C), TensorBoard(log_dir='./tensorboard', histogram_freq=1)]
        nb_train = self.C['nb_train']
        history = self.model.fit(self.X[:nb_train], self.Y[:nb_train], callbacks=cbs)
        values = history.history[self.C['metric']]
        best = eval(self.C['result_mode'])

        return best(values)
