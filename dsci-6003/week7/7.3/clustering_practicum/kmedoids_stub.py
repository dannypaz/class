__author__ = 'you'


import numpy as np
from scipy.spatial.distance import euclidean, cityblock

class KMedoids:
    '''
        Performs PAM clustering and fit. Stores initial clustering as self.clusters. Also provides a predict method.
    '''

    # I give you the constant block here
    def __init__(self, k=1, max_iter=10000, dist=cityblock):
        self.k = k # k has the same meaning as it does in KMeans
        self.max_iter =  max_iter# This is a stopping condition only used in case of nonconvergence
        self.cluster_centers_ = None # These are centers but not medoids
        self.dist = dist
        self.medoids = None # this is the array of medoid assignments
        self.clusters_ = None # this is the array of cluster assignments
        self.D = None # This is the matrix of distances ( you do not have to use this )
        self.scores = [] # stores the scores of each cluster

    # This function is optional. You do not have to use it, but you will need to compute distances somehow.
    def _compute_dist_matrix(self, X):
        '''
            X: m x n 2-d numpy array
            Returns a distance matrix.
        '''

        pass


    @staticmethod
    def _configuration(X, D, clusters, medoids):
        '''
            X: m x n 2-d numpy array
            D: m x m 2-d numpy array
            clusters: 1-d numpy array of length m
            medoids: 1-d numpy array of length k

            Returns cost as a sum of distances to their respective medoids and performs clustering
        '''

        # * you'll want to store the cost of this configuration
        # * you'll need to store the temporary configuration somehow
        # * for each member of the data set
            # * assign the data point the medoid closest to it.
            # * add this distance to the cost

        # * you'll want to return the cost for this configuration and the cluster assignments
        pass


    # The following two functions are optional and you do not have to use them.
    @staticmethod
    def _swap_out(medoids, m, index):
        '''
            medoids: 1-d numpy array of length k
            m: int
            index: int

            Swaps medoid m in place with a chosen member "index" belonging to the dataset.
            Returns the swapped index and medoid
        '''
        pass

    @staticmethod
    def _swap_back(medoids, m, swapped_medoid):
        '''
              medoids: 1-d numpy array of length k
              m: int
              swapped_medoid: int

              Swaps medoid m in place with the index number of the swapped medoid
        '''
        passs

    def fit(self, X):
        '''
            X: m x n 2-d numpy array

            Performs clustering and returns self.cluster_centers_
        '''
        # * precompute distances matrix (you may choose not to)

        # * randomly select k medoids from among the X

        # * randomly assign medoids

        # * mark the cluster centers

        # Keep reconfiguring the medoids until a local minimum is found. This algorithm should converge quite rapidly.

        # * keep track of iterations and provide a stopping point (self.max_iter) to stop nonconverging loops.

            # * you'll need to store the original medoids for comparison somehow

            # * following the pseudocode exactly: iterate over all medoids and nonmedoid points

                        # * swap out the current medoid with another point

                        # * calculate new cost (and clustering configuration)

                        # * if this configuration has a lower cost than the current cost

                            # * store the new cost and clusters as the current clusters

                            # * you may also keep the current score for plotting
                        else:
                            # * if you actually swapped and recalculated the configuration in place
                            # * you'll need to swap it back

            # * if the medoids have stopped changing, stop optimization

        # * at the end of the optimization, store the coordinates of the final medoids.

    # I give this predict block to you
    def predict(self, X):
        '''
            X: m x n 2-d numpy array
        '''

        y_pred = []
        for row in X:
            distance_from_centers = [self.dist(row, center) for i, center in enumerate(self.cluster_centers_)]
            y_pred.append(np.argmin(distance_from_centers))

        return np.array(y_pred)

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt

    n_samples = 130
    np.random.seed(42)
    from sklearn import cluster, datasets
    from sklearn.neighbors import kneighbors_graph
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans as sKMeans

    X,y = datasets.make_blobs(n_samples=n_samples, cluster_std=1.0, random_state=3)
    X = StandardScaler().fit_transform(X)
    X.shape
    colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
    colors = np.hstack([colors] * 20)
    pam = KMedoids(k=3)
    pam.fit(X)  
    plt.scatter(X[:, 0], X[:, 1], color=colors[pam.clusters].tolist(), s=10)
    plt.show()
    plt.clf()
    plt.plot(pam.scores)
    plt.show()
