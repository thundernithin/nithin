# importing the module
import tweepy
 
# personal details
consumer_key ="xxxxxxxxxxxx"
consumer_secret ="xxxxxxxxxxx"
access_token ="xxxxxxxxx"
access_token_secret ="xxxxxxxxx"
 
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
