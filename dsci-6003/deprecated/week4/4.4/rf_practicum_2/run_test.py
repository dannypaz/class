# You can run this script and see the results. Example output is also included
# for each question. Note that there is randomness involved (both in how the
# data is split and also in the Random Forest), so you will not always get
# exactly the same results.


from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from roc import plot_roc


# * 1. Load the dataset in with pandas

# * 2. Convert the "no", "yes" values to booleans (True/False)

# * 3. Remove the features which aren't continuous or boolean

# * 4. Make a numpy array called y containing the churn values

# * 5. Make a 2 dimensional numpy array containing the feature data (everything except the labels)

# * 6. Use sklearn's train_test_split to split into train and test set

# * 7. Use sklearn's RandomForestClassifier to build a model of your data

# * 8. What is the accuracy score on the test data?
## answer: 0.9448441247

# * 9. Draw a confusion matrix for the results
## answer:  716   6
##           40  72

# * 10. What is the precision? Recall?
## precision: 0.923076923077
##    recall: 0.642857142857

# * 11. Build the RandomForestClassifier again setting the out of bag parameter to be true
##   accuracy score: 0.953237410072
## out of bag score: 0.946778711485   (out-of-bag error is slightly worse)

# * 12. Use sklearn's model to get the feature importances
## top five: ['Day Mins', 'CustServ Calls', 'Day Charge', "Int'l Plan", 'Eve Mins']
## (will vary a little)

# * 13. Calculate the standard deviation for feature importances across all trees

# * Print the feature ranking
print("Feature ranking:")


# * Plot the feature importances of the forest - just use the below code
plt.figure()
plt.title("Feature importances")
plt.bar(range(10), importances[indices], yerr=std[indices], color="r", align="center")
plt.xticks(range(10), indices)
plt.xlim([-1, 10])
plt.show()

# * 14. Try modifying the number of trees in blocks of 5 up to 100. Where does accuracy level off?

# * 15. Run all the other classifiers that we have learned so far in class including yours using the below given function

def get_scores(classifier, X_train, X_test, y_train, y_test, **kwargs):
    model = classifier(**kwargs)
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    return model.score(X_test, y_test), \
           precision_score(y_test, y_predict), \
           recall_score(y_test, y_predict)

print "16. Model, Accuracy, Precision, Recall"
print "    Random Forest:", get_scores(RandomForestClassifier, X_train, X_test, y_train, y_test, n_estimators=25, max_features=5)
print "    Logistic Regression:", get_scores(LogisticRegression, X_train, X_test, y_train, y_test)
print "    Decision Tree:", get_scores(DecisionTreeClassifier, X_train, X_test, y_train, y_test)
print "    SVM:", get_scores(SVC, X_train, X_test, y_train, y_test)
print "    Naive Bayes:", get_scores(MultinomialNB, X_train, X_test, y_train, y_test)
## MODEL               ACCURACY PRECISION    RECALL
## Random Forest         0.9508    0.8817    0.7321
## Logistic Regression   0.8741    0.6129    0.1696
## Decision Tree         0.9209    0.6949    0.7321

# * 16. Use the included `plot_roc` function to visualize the roc curve of each model

