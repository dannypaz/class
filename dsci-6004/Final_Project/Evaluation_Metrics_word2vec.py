__author__='Jonathan Hilgart'

from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import re
import textblob
from textblob import TextBlob
import gensim

def accuracy_score_test(list_of_lists_of_queries,story_chunk_responses,item_keyword,type_of_evaluation):
	"""Calculate the accuracy of return the correct response from each story chunk given the keyword of the item the user input"""
	if type_of_evaluation=='tfidf':
		number_correct=0
		number_incorrect=0
		incorrect = []
		correct = []
		for idx,query in enumerate(list_of_lists_of_queries):
			tfidf= TfidfVectorizer()  #create a model
			tf_idf_story= tfidf.fit_transform(story_chunk_responses) ##tf-idf on the possible story chunks in storychunk_one
			query_tfidf = tfidf.transform(query) ## turn the user sentence into a vector
			cosine_sim = linear_kernel(tf_idf_story,query_tfidf).flatten() ## cosine similarity between the story chunks and user sentence
			section = re.sub(r'(\t)','',story_chunk_responses[cosine_sim.argsort()[::-1][0]] )
			if item_keyword in section:
				number_correct+=1
				correct.append(idx)
			else:
				number_incorrect+=1
				incorrect.append(idx)
		if number_incorrect !=0:

			return 'The accuracy is',float(number_correct/(number_correct+number_incorrect)),'The query that failed was :',[list_of_lists_of_queries[i] for i in incorrect]
		else:
			return 'The accuracy is',float(number_correct/(number_correct+number_incorrect)),'The correct queries are',[list_of_lists_of_queries[i] for i in correct]
		#return "The accuracy is :{}".format(number_correct/(number_incorrect+number_incorrect))
	elif type_of_evaluation =='jaccard':
		number_correct=0
		number_incorrect=0
		incorrect = []
		correct = []
		for query_idx,query in enumerate(list_of_lists_of_queries):
			tokens = TextBlob(query[0]).tokens
			query_set = set(tokens)
			len_query = len(query_set)	
			top_score = 0
			response_idx = 0
			for idx,chunk in enumerate(story_chunk_responses):
				story_tokens = TextBlob(chunk).tokens
				jaccard_story= set(story_tokens) ##create a set of the words in the story
				len_chunk = len(jaccard_story)
				len_intersection = len(jaccard_story.intersection(query_set))
				query_score = len_intersection  / (len_query+len_chunk) ## jaccard similarity
				if query_score > top_score:
					top_score=query_score ## replace with the best new match
					response_idx=idx
			if item_keyword in story_chunk_responses[response_idx]:
				number_correct+=1
				correct.append(list_of_lists_of_queries[query_idx])
			else:
				number_incorrect +=1
				incorrect.append(list_of_lists_of_queries[query_idx])
		if number_incorrect !=0:
			return 'The accuracy is',float(number_correct/(number_correct+number_incorrect)),'The query that failed was :',incorrect
		else:
			return 'The accuracy is',float(number_correct/(number_correct+number_incorrect)),'The correct queries are',correct
# See top related words from word2vec model
def word2vec(story_chunk,user_query):
	"""Return the top related words to a user's query"""
	try:
	    one = ''
	    for i in story_chunk:
	        one+=i
	    blob_one= textblob.TextBlob(one)
	    sent_one = [i.tokens.lower() for i in blob_one.sentences]
	    one = one.lower()
	    membership = blob_one.tokens.lower()
	    query_words_one = user_query[0].lower().split(' ')
	    final_query_one=[]
	    count_one = 0
	    ### Check if the user input words are in our word2vec model, if not, we can not use them.
	    for input_one in query_words_one:
	        if input_one in membership:
	            final_query_one.append(input_one)
	    model_one = gensim.models.Word2Vec(sent_one, min_count=1)
	    print('The words most similar (in the given story chunk) to the following query words (vectors added together):',final_query_one)
	    return model_one.most_similar(positive=final_query_one)
	except:
		'There are no words in the story chunk that matches your input.'
