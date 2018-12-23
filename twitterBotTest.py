# 20181223 - Sryn
# Testing Twitter eiKanjiBot App using Tweepy
# using https://tweepy.readthedocs.io/en/3.7.0/getting_started.html 

import tweepy
import config

auth = tweepy.OAuthHandler(
    config.TwitterAPI['API-key']
    , config.TwitterAPI['API-secret-key']
)
auth.set_access_token(
    config.TwitterAPI['Access-token']
    , config.TwitterAPI['Access-token-secret']
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
numTweet = 0
for tweet in public_tweets:
    print(tweet.text)
    numTweet += 1

api.update_status('Downloaded ' + str(numTweet) + ' tweets')
print 'Done'
