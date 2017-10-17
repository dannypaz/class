# Lab Feedback

## Week1-1: Welcome and NLP Overview
Looks Good
## Week1-2: Text Processing & Regular Expressions I
Looks Good
## Week1-3: Regular Expressions II
SpamLord:
Glad to see you're writing your own test cases

```python
#make one email regex by joining all the other patterns
emailregex = "|".join([test_patternemail_1,test_patternemail_2,test_patternemail_3])

for line in f:
    matches = re.findall(emailregex,line)
    matches_phone = re.findall(test_patternphone_1, line)

  #now you only need one for loop
  for match in matches:
       print(match,'match --- longform 8')
       email= '{}@{}'.format(*match)
       results.append((name,'e',email))

  for match in matches_phone:
      print(match,'match  phone-------')
      if match[0][0]=="(":
          area_code = match[0][1:4]
      else:
          area_code = match[0]

      try:
          phone= '{}-{}-{}'.format(area_code,match[1],match[2])
          results.append((name,'p',phone))
      except:
          print('failed')

```
## Week1-4: Segmenting, Tokenizing, & Stemming
Looks Good
## Week2-1: Text Encoding
Looks Good
## Week2-2: Edit Distance
```python
if c1==c2:
    # substitutions =previous_row[j]+0
    # there is no need to add a 0
    substitutions = previous_row[j]
else:

    substitutions =previous_row[j]+1 # TODO: WRITE CODE TO DETEMINE SUBSTITUTION
```

## Week2-3: Language Modeling I
TODO: Why does the probability of this phrase go down with bigram word?

The probability goes down because "the the" does not appear often in the corpus. Thus the model interprets this as a low probability of seeing "the the"


TODO: Why does the probability of this phrase go way up with bigram word?

the bigrams "Of the" and "the same" are seen a lot in our corpus, thus they have a high probability of occurring. However, the product of the unigrams "of", "the" and "same" are lower because one of those words isn't seen a lot in our corpus.
## Week2-4: Language Modeling II
```python
def word_data(blob):
    memo = ()
    counts = []

    vocab = set()

    for tok in blob.tokens:
        if tok not in vocab:
            vocab.add(tok)
        #calculating len(vocab) every iteration is wasteful
        counts.append(len(vocab))

    #going through the entire list again is wasteful
    return[(i+1,counts[i]) for i  in range(len(counts))]

def word_data(blob):
    ans = []
    counts = []

    vocab = set()
    vocab_len = 0

    for tok in blob.tokens:
      #if word not in vocab, add word to vocab and increase vocab length by 1
        if tok not in vocab:
            vocab.add(tok)
            vocab_len += 1
        #append each new answer to the output list as a tuple
        ans.append((i+1,len(vocab)))
    return ans
```
## Week3-1: Spelling Correction
```python
with open('../../corpora/spell_errors.txt') as t:
    spelling = t.read()

spelling = re.split('\n|:',spelling)
spelling = [item.replace('_',' ') for item in spelling]
spelling = [item.strip(' ') for item in spelling]

#you went through t once, and spelling twice, this is inefficient
#you should only go through the list once
spell_errors = {}
with open("../../../corpora/spell_errors.txt") as f:
    for line in f: #this goes through f once
        correct, errors = line.split(":")
        spell_errors[correct.replace("_", " ")] = errors.strip().split(", ")  
```
## Week3-2: Word Tagging
You don't need to create a default tagger function, nltk has one

## Week3-3: Named Entity Recognition (NER)
Looks Good
## Week3-4: Review/Project Check In

## Week4-1: Information Retrieval I
Looks Good
## Week4-2: Information Retrieval II
```python
#don't do this
top = (1.0 + math.log10(q_count[word]))* self.get_tfidf(word,d_idx)
num += top

#do this
top += (1.0 + math.log10(q_count[word]))* self.get_tfidf(word,d_idx)

 # no need to have num or den variable
```
## Week4-3: Information Retrieval Project

## Week4-4: Chatbots I
use list.insert() method to add different options to pyschobable
## Week5-1: Chatbots II
Looks Good
## Week5-2: Naive Bayes
Looks Good
## Week6-1: Sentiment Analysis
Looks Good
## Week6-2: Non-negative Matrix Factorization (NMF)
Topic 0 is to general to give it a topic. However the other 3 seem really specific. This is an indicator that you should try more topics.
## Week6-3: Latent Dirichlet Allocation (LDA)
Looks Good
## Week6-4: Topic Modeling Project

## Week7-1: Word2Vec
Looks Good
## Week7-2: Doc2Vec

## Week7-3: Everything2Vec

## Week7-4: Future of NLP Guest Lecture

## Week8: Final Presentation:
