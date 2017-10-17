from trainers import *
from sacred import Experiment

ex = Experiment()


@ex.config
def my_config():
    trainer = 'MLRTrainer'
    optimizer = 'sgd'
    metric = 'loss'
    result_mode = 'min'
    nb_train = 1_000

@ex.automain
def main(_config, _run):
    """Run a sacred experiment

    Parameters
    ----------
    _config : special dict populated by sacred with the local variables computed
    in my_config() which can be overridden from the command line or with
    ex.run(config_updates=<dict containing config values>)
    _run : special object passed in by sacred which contains (among other
    things) the name of this run

    This function will be run if this script is run either from the command line
    with

    $ python train.py

    or from within python by

    >>> from train import ex
    >>> ex.run()

    """
    _config['name'] = _run.meta_info['options']['--name']

    trainer = eval(_config['trainer'])(_config)
    trainer.load_data()
    trainer.build_model()
    trainer.compile_model()
    result = trainer.fit()

    return result
