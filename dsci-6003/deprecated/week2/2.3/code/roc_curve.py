from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
import numpy as np


def roc_curve(probabilities, labels):
    '''
    INPUT: numpy array, numpy array
    OUTPUT: list, list, list

    Take a numpy array of the predicted probabilities and a numpy array of the
    true labels.
    Return the True Positive Rates, False Positive Rates and Thresholds for the
    ROC curve.
    '''

    '''#Following Algorithm 2 from
    http://www.hpl.hp.com/techreports/2003/HPL-2003-4.pdf '''

    '''#Initialize lists'''
    TPRs = []
    FPRs = []
    treshholds = []

    '''#Count number of positive and negative cases'''
    num_pos_cases = list(labels).count(1)
    num_neg_cases = list(labels).count(0)

    '''#Sort probabilities by desc order'''
    sorted_probabilities = sorted(probabilities, reverse=True)

    '''#Sort indexes of probabilities by desc order,
    this will help to match indices of labels'''
    sorted_indices = np.argsort(probabilities)[::-1]
    sorted_labels = labels[sorted_indices]

    '''#Intialize true positives and false positives counter'''
    '''#true positives'''
    tp = 0.0
    '''#false positives'''
    fp = 0.0
    '''#auxiliary var'''
    prev_prob = float("inf")

    for prob in sorted_probabilities:

        '''#Append values of prob into treshholds list '''
        treshold = prob
        treshholds.append(treshold)

        for i, label in enumerate(sorted_labels):

            '''#Check if prob of label is not equal to treshold '''
            if probabilities[i] != prev_prob:
                '''#if the index is not equal to zero then
                append values into TPRs and FPRs lists'''
                if i != 0:
                    TPRs.append(tp/num_pos_cases)
                    FPRs.append(fp/num_neg_cases)
                '''Replace value of prev_prob with  prob of label[i] '''
                prev_prob = probabilities[i]

            '''#If label is positive then increase the counter of tp ,
            otherwise increase the fp counter'''
            if label == 1:
                tp += 1.0
            else:
                fp += 1.0

        '''#Calculate true positives rate and false negative rate '''

        '''#true_positives= number correctly predicted
        true positives/ number of positive cases'''
        TPRs.append(tp/num_pos_cases)

        '''#true_positives= number incorrectly predicted true positives/
        number of negative cases'''
        FPRs.append(fp/num_neg_cases)

    return FPRs, TPRs, treshholds


def main():

    X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           n_clusters_per_class=2, n_samples=1000)

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    probabilities = model.predict_proba(X_test)[:, 1]

    fpr, tpr, thresholds = roc_curve(probabilities, y_test)

    plt.plot(np.asarray(fpr), np.asarray(tpr))
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.xlabel("False Positive Rate (1 - Specificity)")
    plt.ylabel("True Positive Rate (Sensitivity, Recall)")
    plt.title("ROC plot of fake data")
    plt.show()


if __name__ == '__main__':
    main()
