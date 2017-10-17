RAT Solutions
--------

1) MLlib has:
- logistic regression and linear support vector machine (SVM)
- classification and regression tree
- random forest and gradient-boosted trees
- recommendation via alternating least squares (ALS)
- clustering via k-means, bisecting k-means, Gaussian mixtures (GMM), and power iteration clustering
- topic modeling via latent Dirichlet allocation (LDA)
- survival analysis via accelerated failure time model
- singular value decomposition (SVD) and QR decomposition
- principal component analysis (PCA)
- linear regression with L1, L2, and elastic-net regularization
- isotonic regression
- multinomial/binomial naive Bayes
- frequent itemset mining via FP-growth and association rules
- sequential pattern mining via PrefixSpan
- summary statistics and hypothesis testing
- feature transformations
- model evaluation and hyper-parameter tuning

2) MLlib doesn't have:
- Deep Learning
-  

3) K-means is a good fit for Spark because:
1. It is very common. Spark wants wide spread adoption.  
2. It requires a complete pass over the data every iteration. Spark is relatively efficient for that specification.

4) Explain how ALS differs from SVD.

Both involve low-rank approximate factorizations.

ALS: generic approach which can be combined with many factorizations:   Singular value decomposition: specific factorization 

Alternating least squares is flexible but less precise. It refers to any means of of factoring  A≈XkYTkA≈XkYkT , where  XkXk  and  YkYk  are low rank. "Approximate" means minimizing some squared-error difference with the input A, but, here you can customize exactly what is considered in the loss function. For example you can ignore missing values (crucial) or weight different  AijAij  differently. The price is that you don't get many guarantees about the two factors. They are not necessarily orthonormal. In practice it does not help, but doesn't hurt much.

In contrast the SVD is a particular decomposition that gives more guarantees about its factorization A=UΣVTkA=UΣVkT. The two outside factors are orthornormal for example. ΣΣ will even help show you how big k should be.

The cost is speed and flexibility. The SVD is relatively more computationally expensive and harder to parallelize. There is also not a good way to deal with missing values or weighting; you need to assume that in your sparse input, missing values are equal to a mean value 0. 

https://www.quora.com/What-is-the-difference-between-SVD-and-matrix-factorization-in-context-of-recommendation-engine

http://spark.apache.org/docs/latest/mllib-collaborative-filtering.html

http://spark.apache.org/docs/latest/mllib-dimensionality-reduction.html

__Optional__) How does MLlib distribute data in Spark in order to parallelize matrix factorization?
    Cache 2 copies of R in memory, one partitioned by rows and one by columns
    Keep U & V partitioned in corresponding way

    http://spark.apache.org/docs/latest/mllib-data-types.html#distributed-matrix

    http://stanford.edu/~rezab/slides/reza_codeneuro.pdf
---
extra questions
---

3) Why did MLlib developers pick Stochastic gradient descent (SGD) as the first optimization method? What are the pros and cons?

Basically, instead of summing over all the training examples and then computing the gradient like in ordinary gradient descent, in stochastic gradient descent, the gradient is computed and the weights are updated for each training example. You can think of this as taking small steps down the slope, at each training example, which is far more efficient than ordinary gradient descent (which is not practical for large datasets). Here is pseudo-code to illustrate this:

while (iter < maxIter)
{

   for i = 1... # of training examples
   {
        compute gradient
        update weights
   }

   iter++
}

Note that stochastic gradient descent, as the name suggests, is stochastic. That means that the minima where it ends up is completely random and depends on the weight initialization. Usually it takes a lot longer for stochastic gradient descent to converge to a global minimum than gradient descent, but gives a good solution much faster, for obvious reasons.

https://www.quora.com/How-does-stochastic-gradient-descent-work

1) What RDD type would you use when applying logistic regression? Why?  
&nbsp;&nbsp;A. LabeledPoint  
&nbsp;&nbsp;B. Pair RDD  
&nbsp;&nbsp;C. Vector  
&nbsp;&nbsp;D. Rating  

    A) 1. LabeledPoint. Each vector needs to have an associated label

2. Which of these statistics are provided by `Statistics.colStats` in MLlib?
    1. minimum
    2. lower quartile
    3. median
    4. arithmetic mean
    5. geometric mean
    6. 75th percentile
    7. maximum
    8. variance

2. Which of these statistics are provided by `Statistics.colStats` in MLlib?
    A) 1. minimum, 4. arithmetic mean, 7. maximum, 8. variance


2. Which algorithm would you use for factorizing matrices with missing values?
    1. Singular Value Decomposition
    2. Support Vector Machines
    3. Factor Analysis
    4. Alternating Least Squares

3. Which algorithm would you use for factorizing matrices with missing values?
    A) Alternating Least Squares