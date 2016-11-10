# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk
import random
from nltk.book import *
from nltk.corpus import gutenberg
from nltk import word_tokenize, sent_tokenize

tagged_tokens = nltk.pos_tag(text2)

print('Original text (150 tokens)')
requir_1 = tagged_tokens[:150] #tuples

#print (requir_1) #pritns 150 characters/tokens

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

list1 = []

for (word,tag) in requir_1:
	list1.append(spaced(word))
print ("".join(list1)) #taking the words in the list and putting it in an empty string

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"JJ":.1}

final_words = []

#madlib_generator from .py file
for (word, tag) in tagged_tokens[:150]: #up to 150 or list goes on and on 
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words)) #madlib_generator

