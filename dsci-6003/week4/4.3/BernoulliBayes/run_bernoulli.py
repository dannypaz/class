'''
In this file, test your scores against those of sklearn's. Use KFold with 5 folds. 
'''

from bernoulli_JH import BernoulliBayes
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.model_selection import KFold
import numpy as np
from math import sqrt
from sklearn.metrics import accuracy_score


def evaluate_code(X,y,folds,a):
	"""Evalute Bernouli bayes using my implementation vs Sklearn's implementation"""
	# first use my implementation
	my_rmse = []
	my_accuracy = []
	sk_rmse = []
	sk_accuracy = []
	multi_rmse = []
	multi_accuracy = []
	k_val =  KFold(folds)
	for train_idx, test_idx in k_val.split(X):
	    X_train, X_test = X[train_idx], X[test_idx]
	    y_train, y_test = y[train_idx], y[test_idx]
	    my_bernouli = BernoulliBayes()
	    my_bernouli.fit(X_train,y_train)
	    my_rmse.append(np.linalg.norm(y_test-my_bernouli.predict(X_test))/sqrt(len(y_test)))
	    sk_bernouli = BernoulliNB()
	    sk_bernouli.fit(X_train,y_train)
	    sk_rmse.append(np.linalg.norm(y_test-sk_bernouli.predict(X_test))/sqrt(len(y_test)))
	    my_accuracy.append(accuracy_score(y_test ,my_bernouli.predict(X_test)))
	    sk_accuracy.append(accuracy_score(y_test ,sk_bernouli.predict(X_test)))
	    multi_NB = MultinomialNB(alpha=1)
	    multi_NB.fit(X_train,y_train)
	    multi_accuracy.append(accuracy_score(y_test ,multi_NB.predict(X_test)))
	    multi_rmse.append(np.linalg.norm(y_test-multi_NB.predict(X_test))/sqrt(len(y_test)))

	print('My RMSE Score (Binomial NB) {}'.format(np.mean(my_rmse)))
	print('My accuracy score (Binomial NB):{:.2%}'.format(np.mean(my_accuracy)))
	print('SKlearn RMSE (Binomial NB):{}'.format(np.mean(sk_rmse)))
	print('SKlearn Accuracy (Binomial NB):{:.2%}'.format(np.mean(sk_accuracy)))
	print('SKlearn Multi NB RMSE with {} threshold:{}'.format(a,np.mean(multi_rmse)))
	print('SKlearn Multi NB Accuracy with {} threshold:{:.2%}'.format(a,np.mean(multi_accuracy)))


