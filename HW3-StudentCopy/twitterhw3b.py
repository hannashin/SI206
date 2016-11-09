# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import json
import requests
from textblob import TextBlob
import tweepy

# Unique code from Twitter
access_token = "791353725814247424-47MAYDihAZkKKwTWEXN7t7tP3QSiUfQ"
access_token_secret = "kdR2sWdWQACULBBGo73V9Yg3CMgVlR6CZVxxhwUM7qrys"
consumer_key = "ifKlPItpKpgVo9ZKND55OsqIW"
consumer_secret = "cfB9sVlHWt94DqJnDf86FBIq46lfWXWSEC4ClibCoUtMdbZEpo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_results = api.search(q='Twizzlers') #Twizzlers
#length of the comp
comp = [tweet.text for tweet in search_results]
type(comp)

print (comp) #prints each tweet

#Using textblob documentaries

subjectivity_count = 0 #returns a float
polarity_count = 0 #returns a float
for words in comp:
	a = TextBlob(words)
	subjectivity_count += a.subjectivity #documentations
	polarity_count += a.polarity #documentations


print("Average subjectivity is " + str(subjectivity_count/len(comp))) #divide by average str
print("Average polarity is " + str(polarity_count/len(comp))) #divide by average

#YOUNG SAVAGE!!!!!!!!!!!!!!!!!!
