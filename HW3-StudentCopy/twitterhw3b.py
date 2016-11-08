# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.


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

search_results = api.search(q='Jubilee') 

comp = [tweet.text for tweet in search_results]

print (comp)


print("Average subjectivity is")
print("Average polarity is")
