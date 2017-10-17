import numpy as np


class Bandits(object):
    '''
    This class represent n bandit machines.
    '''

    def __init__(self, p_array):
        '''
        INPUT: list of floats
        OUTPUT: None

        Takes a list of probabilities (probability of conversion) and
        initializes the bandit machines.
        '''
        self.p_array = p_array
        self.optimal = np.argmax(p_array)
        
    def pull(self, i):
        '''
        INPUT: 
        OUTPUT: Bool

        Returns True if the choosing the ith arm led to a conversion.
        '''
        return np.random.random() < self.p_array[i]
    
    def __len__(self):
        return len(self.p_array)
