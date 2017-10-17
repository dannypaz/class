from sacred import Experiment
ex = Experiment('test')

from trainers import *


@ex.config
def my_config():
    trainer = 'MLRTrainer' # architecture
    loss = 'categorical_crossentropy' # type of loss
    hidden_size = 128 # number of units in hidden layer
    reg = 1e-6
    epochs = 5
    frontend = 'jupyter' # set to 'cmd' when calling from the command line!

@ex.automain
def main(_config):
    """Run a sacred experiment

    Parameters
    ----------
    _config : special dict populated by sacred with the local variables computed
    in my_config() which can be overridden from the command line or with
    ex.run(config_updates=<dict containing config values>)

    This function will be run if this script is run either from the command line
    with

    $ python train.py

    or from within python by

    >>> from train import ex
    >>> ex.run()

    """
    trainer = eval(_config['trainer'])(_config)
    trainer.load_data()
    trainer.build_model()
    trainer.compile_model()
    trainer.fit()
