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

#PART 1

import nltk
import random
from nltk.book import *
from nltk.corpus import gutenberg
from nltk import word_tokenize, sent_tokenize

tagged_tokens = nltk.pos_tag(text2)
