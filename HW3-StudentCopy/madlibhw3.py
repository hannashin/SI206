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

print('Original text (150 tokens)')
requir_1 = text2[:150]

#print (requir_1) #pritns 150 characters/tokens

def spaced(speech):
	if speech in [',','.','!',':','?']:
		return speech
	else:
		return " " + speech



