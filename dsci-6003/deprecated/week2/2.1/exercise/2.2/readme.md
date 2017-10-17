# Tuning and Model Comparison

Try to run each of these other classifiers over the dataset and compare the results. We're going to start with the pickle file `data/data.pkl`. This dataset has 1405 articles.

1. Load in the data from the pickle file:

    ```python
    import cPickle as pickle

    with open('data/data.pkl') as f:
        df = pickle.load(f)
    ```

2. To create the label vector `y`, use sklearn's [LabelEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) to convert the strings to integers. 

3. For all of your models, you should use [TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to create a feature matrix of the text.

    Tf-idf will create a feature matrix where each word is a feature.

    **Note:** You should fit the tfidf vectorizer on the *training set only*! Don't use the test set to build your training feature matrix, or you are using the test set to help build your model! You should do something like this, if `data` is a list of strings of the text of the documents.

    ```python
    data_train, data_test = data[train_index], data[test_index]
    tfidf = TfidfVectorizer()
    X_train = tfidf.fit_transform(data_train)
    X_test = tfidf.transform(data_test)
    ```

4. Use sklearn's implementation of Naive Bayes: [MultinomialNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html). Use cross validation to find the optimal value for the laplace smoothing constant.

5. Try running the classifiers we have learned (will learn) about so far:

    * Logistic Regression
    * kNN
    * Naive Bayes

    Note that to use some of these models, you will need to use tactics to deal with multiple classes. Logistic Regression only works on binary predictions. kNN and Naive Bayes are naturally multiclass. There are two techniques for dealing with making multiclass classification problems into binary problems:

    * One-Vs-All: For each of the labels, build a model which predicts True or False for that label. (faster!)
    * One-Vs-One: For each pair of labels, build a model which predicts which of those two labels is more likely.

    Sklearn has these implemented already, and you can read about them [here](http://scikit-learn.org/stable/modules/multiclass.html).

    In the interest of time, use any cross validation technique you see fit.

    Which models get the best accuracy?

    If you have time, do a grid search to get the best parameters for each model so you can do a fair comparison.

6. Use the `time` module to get the runtime of each of the models like this:

    ```python
    import time

    start = time.time()
    # do some stuff
    end = time.time()
    print "total time:", end - start
    ```

    Which models are the fastest to train? To predict?

7. Instead of using KFold, use [LeaveOneOut](http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.LeaveOneOut.html). This is more time consuming but maybe gets a better measure of the score. This will take a few hours to run, so don't just sit there waiting! It's sometimes worth doing if you have the time and want the accuracy, but it's worth understanding the tradeoffs.