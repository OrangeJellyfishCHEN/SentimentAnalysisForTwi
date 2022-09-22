import tweepy
from dotenv import load_dotenv

consumer_key = "JIdqvHzIyQcTXbpNAE7eoLZLR"
consumer_secret = "w1RLvzQJMFyk4dznROXk9J2m6hTgf4ngtj4bEFrx9s6iY5RPr0"
access_token = "1571291635618844676-e1ggQHw9zKkKkl59Q5IH2enYmDRHeC"
access_token_secret = "UQeTd3lixkEBXirDGxBAJu8sSDSzTZkM8BMjTeMpCzqd3"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# This is an example for finding tweets that contain the word iphone
for tweet in api.search_tweets(q="iphone", lang="en"):
    print(tweet.text)
