Machine Learning I Final Project
===

For your final project, you will pick one of the user review datasets from [Text Analytics](http://www.text-analytics101.com/2011/07/user-review-datasets_20.html) or you may pick another dataset upon agreement with your 6004 instructor. Every non-Text Analytics dataset must be approved by both your 6003 and 6004 instructor.

First, perform basic Exploratory Data Analysis (EDA) and preprocessing. Since this is a text-based project, a certain amount of NLP will be required.

Second, produce a model of your data <a name="myfootnote1"><sup>1</sup></a> using a classifier of your choice.

Third, visualize your data and model appropriately.

Fourth, take the source code of your model - i.e. the source of the scikit classifier you are using, or if you are using your own model (one we have taught in class), and provide complete annotation and critique along the lines of our practicum grading sections.

Explore each of the following steps and document your efforts:

### Part I Preprocessing and EDA 


Address each of the following topics in a typed document (either .ipynb or .md) to be determined after you have found some success with your dataset:

__Exploratory Data Analysis (EDA)__:

- What specific munging issues do you have to address (e.g., encoding or missing data)?
- What statistical methods are useful for understanding your data?
- Construct useful figures using a plotting method. Explain why you have chosen to represent the data this way.

### Part II Construction and Validation of the Model

__Model__: 

- What model(s) did you choose? Why? 
- For the models that you chose, find the code that implements the models. Annotate the code by placing letters near each operation in the code that corresponds with the math used to describe the model. On a separate document (.txt) add descriptions to each letter, describing the math and reasoning behind each step of the model. 

__Normalization__: 

- Did you normalize your tokens in any way (case, stemming, lemmatization)? If so, how? Why or why not?

__Validation__:

- What forms of validation did you use? (e.g. k-fold cross-validation, etc.) 
- Please note that the same mode of validation may not be appropriate for all models and systems. You need to select a form of validation that is appropriate for your model and system. This may include several different methods of doing so.
- You must provide convincing reasoning grounded in the theory that was discussed in class. This requirement will be taken quite seriously and will be graded on completeness and seriousness of response.

__Scoring__:

- Pick at least 2 metrics to score your model: (e.g. accuracy, F1, AUC, etc.) Why did you use these? Explain why these metric were a valuable part of your evaluation. Are there other metrics you could have used instead? Why didn’t you choose those? Describe the basic theory behind the metric in your own words (you may need to do additional research). This requirement will be taken quite seriously and will be graded on completeness and seriousness of response.

__Ensemble and/or Boosted Models__: 

- Did you try any ensemble methods or boosted models? If so, which ones? Did they help? Why/why not? Provide reasoning. 

__Extra Credit__:

- Applied unsupervised methods or a continuous word embedding algorithm (W2V, GloVe,...) to support feature engineering.
- Use an advanced model [FMs for example](http://ssli.ee.washington.edu/~mhwang/pub/2014/fmnn_emnlp2014.pdf) instead one of those we have discussed in class.

***

For each of steps, we want both an empirical and a logical justification for the choices you made. That is: show us that the choice you picked is empirically superior to the alternative (better F1 score, etc.) and explain why you think that is.  

Each step is weighted equally. The only deliverable is an in-class presentation. The presentation style, or lack of style, (e.g., notebooks, code, and slides) will not be scored.

Scoring: 
---			
0) __Missing__ - Didn’t show up or forgot to address that part of the project <br>
1) __Beginning__ - Used default models and parameters. Did __not__ explore any alternatives <br>
2) __Developing__ - Explored alternatives but did not test them <br>
3) __Accomplished__ - Demonstrated that one choice was better than others according to some metric, but no explanation as to why <br>
4) __Exemplary__ - Demonstrated that specific parameters and models were better than others according to some metric and gave a convincing explanation as to why <br>
<br>
<br>
***
<sup>[1](#myfootnote1)</sup> These steps are iterative (a little preprocessing, a little modeling, redo the preprocessing, ...)