# 20181223 - Sryn
# Testing Twitter eiKanjiBot App using Tweepy
# using https://tweepy.readthedocs.io/en/3.7.0/getting_started.html 

import json
import tweepy
import config
import time
import datetime 
# https://www.pythonforbeginners.com/basics/python-datetime-time-examples
# https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

def getAPI():
    auth = tweepy.OAuthHandler(
        config.TwitterAPI['API-key']
        , config.TwitterAPI['API-secret-key']
    )
    auth.set_access_token(
        config.TwitterAPI['Access-token']
        , config.TwitterAPI['Access-token-secret']
    )

    return tweepy.API(auth)

def getAPI2():
    # https://stackoverflow.com/a/19078712

    with open('config.json', 'r') as f:
        config = json.load(f)

    auth = tweepy.OAuthHandler(
        config['TwitterAPI']['API-key'],
        config['TwitterAPI']['API-secret-key']
    )

    auth.set_access_token(
        config['TwitterAPI']['Access-token'],
        config['TwitterAPI']['Access-token-secret']
    )

    return tweepy.API(auth)

def getLastMentionID():
    with open('config.json', 'r') as f:
        config = json.load(f)

    try:
        lastMentionID = config['lastMentionID']
    except:
        lastMentionID = 0

    return lastMentionID

def writeLastMentionID(mentionID):
    config = {'lastMentionID': mentionID}

    with open('config.json', 'w') as f:
        json.dump(config, f)

def updateLastMentionID(mentionID):
    with open('config.json', 'r') as f:
        config = json.load(f)

    #edit the data
    config['lastMentionID'] = mentionID

    #write it back to the file
    with open('config.json', 'w') as f:
        json.dump(config, f)

    print 'Updated lastMentionID to ' + str(mentionID)

def tweetUpdateStatus(api, aString):
    api.update_status(aString)

def tweetReplyStatus(api, aString, statusID):
    print 'Tweeting Back: ' + aString
    api.update_status(aString, statusID)
    # Wait one second to prevent flooding Twitter
    # https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
    time.sleep(1)

def printHomeTimeline(api):
    public_tweets = api.home_timeline()
    numTweet = 0
    for tweet in public_tweets:
        print(tweet.text)
        numTweet += 1
    # api.update_status('Downloaded ' + str(numTweet) + ' tweets')
    updateStatusString = 'Downloaded ' + str(numTweet) + ' tweets'
    tweetUpdateStatus(api, updateStatusString)

def tweetBack(api, status):
    # force to refer to the global variable 
    # https://www.python-course.eu/global_vs_local_variables.php
    # global lastMentionID

    toUser = status.user.screen_name
    strDateTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    msgBody = 'Tweet Back ' + strDateTime
    updateStatusString = '@' + toUser + ' ' + msgBody
    tweetReplyStatus(api, updateStatusString, status.id)

def printMentionsTimeline(api):
    currMaxMentionID = 0
    lastMentionID = getLastMentionID()
    statuses = api.mentions_timeline(lastMentionID)
    numTweet = 1
    for status in statuses:
        # print numTweet + ': ' + str(status.id) + ' - ' + str(status.text)
        # print str(numTweet) + ': ' + str(status.id) + ', status.source - ' + status.source + ', status.user.source - ' + status.user.name + ', status.user.screen_name - ' + status.user.screen_name + ', ' + status.text 
        print str(numTweet) + ': ' + str(status.id) + ', status.user.screen_name - ' + status.user.screen_name + ', ' + status.text 
        numTweet += 1
        tweetBack(api, status)
        if int(status.id) > currMaxMentionID:
            currMaxMentionID = int(status.id)
    
    if currMaxMentionID > lastMentionID:
        updateLastMentionID(currMaxMentionID)

def main():
    # api = getAPI()
    api = getAPI2()

    # printHomeTimeline(api)

    # will overwrite everything with just this one setting
    # writeLastMentionID(datetime.datetime.now().strftime('%y%m%d%H%M%S'))

    # This didn't overwrite everything in there, but have to reformat the EOL
    # Also, if the field isn't there, it'll make one
    # updateLastMentionID(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

    printMentionsTimeline(api)

    print 'Done'

main()