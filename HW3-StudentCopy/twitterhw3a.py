# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

#Twitter Handle : https://twitter.com/206_hanna

import tweepy


# Unique code from Twitter
access_token = "791353725814247424-47MAYDihAZkKKwTWEXN7t7tP3QSiUfQ"
access_token_secret = "kdR2sWdWQACULBBGo73V9Yg3CMgVlR6CZVxxhwUM7qrys"
consumer_key = "ifKlPItpKpgVo9ZKND55OsqIW"
consumer_secret = "cfB9sVlHWt94DqJnDf86FBIq46lfWXWSEC4ClibCoUtMdbZEpo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
api.update_with_media(filename = "koons.jpg", status='#UMSI-206 #Proj3')



#Test 1
#run1 = twtr.tweet("Prints out an image!")
#print (run1) #should return None, but tweets run1 (Prints None on terminal)

# # Boilerplate code here
# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)

# api = tweepy.API(auth)
# #Now we can Create Tweets, Delete Tweets, and Find Twitter Users

# public_tweets = api.search('UMSI')


# for tweet in public_tweets:
# 	print(tweet.text)


# print("""No output necessary although you 
# 	can print out a success/failure message if you want to.""")