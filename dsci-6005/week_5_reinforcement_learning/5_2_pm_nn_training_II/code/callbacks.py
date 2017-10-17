from keras.callbacks import Callback
from datetime import datetime


class AddTimestamp(Callback):
    """Assigns unique ids to metrics for scalar summary visualizations in TensorBoard"""

    def __init__(self, exp):
        self.exp = '+'.join(f'{key}={value}' for key, value in exp.items())
        self.T = datetime.now()

    def on_epoch_end(self, epoch, logs={}):
        for metric in self.params['metrics']:
            logs[f'{metric}:{self.exp}@{self.T}'] = logs[metric]
