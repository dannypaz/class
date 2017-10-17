## Lesson 5: Statistics

![love letter](http://www.mathfunny.com/images/mathjoke-haha-humor-math-meme-joke-pic-mathmeme-funnypics-pun-standarddeviation-statistics-norm-love.jpg)

## Introduction
We are going to implement functions to calculate some basic statistics here. The main goal is to jostle your memory on these statistics, and at the same time gently introduce you to more of the scipy and numpy functionalities.  

As a review, you might go over the following section(s) in the [Khan Academy's probability course](https://www.khanacademy.org/math/probability).  

- [Descriptive statistics](https://www.khanacademy.org/math/probability/descriptive-statistics)

**Optional:**

- [Statistical studies](https://www.khanacademy.org/math/probability/statistical-studies)
- [Regression](https://www.khanacademy.org/math/probability/regression)
- [Inferential statistics](https://www.khanacademy.org/math/probability/statistics-inferential)

## Assignment
Go to the ```lesson_5_statistics``` folder (which holds this README.md) and start IPython notebook with the command ```jupyter notebook``` in the terminal.

Follow the instructions below to fill in ```statistics.ipynb```. 

You will be implementing all the functions at the beginning of the notebook
and will be calling the functions in the last cell, e.g.

```
population = load_pickle('population.pkl')
print('First 5 element of the population: ', population[:5])
sample_100 = draw_sample(population, 100)
sample_1000 = draw_sample(population, 1000)
population_mean = get_mean(population)
sample_100_mean = get_mean(sample)
sample_1000_mean = get_mean(sample)
print('Population mean: ', population_mean)
print('Sample 100 mean: ', sample_100_mean)
print('Sample 1000 mean: ', sample_1000_mean)
...
```

**Before we start, this exercise is meant for you to implement the equations yourself, you should not use the numpy functions ```np.mean()```and ```np.var()``` here. Feel free to use any other numpy /scipy functions as you see fit.**

- Implement ```draw_sample()``` to draw a number of members randomly from the
population.

    - Define a ```sample_100``` variable which draws 100 members at the bottom.

    - Define a ```sample_1000``` variable which draws 1000 members at the bottom.

- Implement ```get_mean()``` to find the mean given an array of numbers.
Call ```get_mean()``` at the bottom to calculate population mean and
sample mean. Print the mean values.

- Implement ```get_median()``` to find the median given an array of numbers. 


- Implement ```get_variance()``` to find the sample variance and population
variance. You will need to have the function take in a ```sample``` parameter which if set to ```True```, will calculate sample variance, otherwise
population variance. Call the function to find both sample and population
variances. Print them out. You should have a population variance, sample 100
variance and sample 1000 variance.

- Implement ```get_standard_deviation()``` to find the sample standard deviation and population standard deviation.

- Implement ```get_range()``` to calculate the range of the data. 


