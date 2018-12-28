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
import unicodedata
import KanjiAliveMP4

defaultHeadLength = len('@eiKanjiBot ')
intervalSeconds = 15.0

# using config.py file
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

# using config.json file thru ConfigParser
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
    # with open('config.json', 'r') as f:
    #     config = json.load(f)
    with open('varConfig.json', 'r') as f:
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
    # with open('config.json', 'r') as f:
    #     config = json.load(f)
    with open('varConfig.json', 'r') as f:
        config = json.load(f)

    #edit the data
    config['lastMentionID'] = mentionID

    #write it back to the file
    # with open('config.json', 'w') as f:
    #     json.dump(config, f)
    with open('varConfig.json', 'w') as f:
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

def getFirstCharacter(statusText):
    global defaultHeadLength

    firstCharacter = '_'
    if len(statusText) > defaultHeadLength:
        statusText = statusText[defaultHeadLength:] # trim the header + one space
        statusText = statusText.strip() # trim whitespaces front and end
        if len(statusText) > 0:
            firstCharacter = statusText[0]

    # try:
    #     firstCharacter = statusText[defaultHeadLength]
    # except:
    #     firstCharacter = '_'

    return firstCharacter

def getFirstCharacterName(aChar):
    rtnString = ''
    if len(aChar) == 1:
        rtnString = unicodedata.name(aChar)
    return rtnString

def getFirstCharacterCategory(aChar):
    return unicodedata.category(aChar)

def getFirstCharacterTypes(aChar):
    rtnString = ''
    if len(aChar) == 1:
        rtnString += '\'' + unicodedata.name(aChar) + '\' '
        # rtnString += unicodedata.decimal(aChar) + ' ' # error if aChar is not a decimal
        # rtnString += unicodedata.digit(aChar) + ' ' # error if aChar is not a digit
        # rtnString += unicodedata.numeric(aChar) + ' ' # error if aChar is not a numeric
        rtnString += '\'' + unicodedata.category(aChar) + '\' '

    return rtnString        

def getFirstCharacterCodePoint(aChar):
    codePoint = ''
    if len(aChar) == 1:
        codePoint = hex(ord(aChar))
    return codePoint

def checkFirstCharacterCJK(aChar):
    rtnBool = False
    if len(aChar) == 1:
        aCharName = getFirstCharacterName(aChar)
        if aCharName[:3] == 'CJK':
            rtnBool = True
    return rtnBool

def tweetBack(api, status):
    # force to refer to the global variable 
    # https://www.python-course.eu/global_vs_local_variables.php
    # global lastMentionID

    toUser = status.user.screen_name
    firstCharacter = getFirstCharacter(status.text)
    # firstCharacterCategory = getFirstCharacterCategory(firstCharacter)
    # firstCharacterTypes = getFirstCharacterTypes(firstCharacter)
    isFirstCharacterCJK = checkFirstCharacterCJK(firstCharacter)
    # firstCharacterCodePoint = getFirstCharacterCodePoint(firstCharacter)
    strDateTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # msgBody = 'Tweet Back ' + firstCharacter 
    # msgBody += ' NaCa: ' + firstCharacterTypes 
    # msgBody += ' CodePoint: ' + firstCharacterCodePoint
    # msgBody += ' isCJK: ' + str(isFirstCharacterCJK)
    # msgBody += ' ' + strDateTime

    if isFirstCharacterCJK:
        # msgBody = firstCharacter
        # msgBody = config.rtnMP4Test(firstCharacter)
        # msgBody = KanjiAliveMP4.rtnMP4Test(firstCharacter)
        msgBody = KanjiAliveMP4.getKanjiAliveMP4(firstCharacter)
        # msgBody += ' ' + strDateTime
    # else:
    #     msgBody = 'Usage: \'@eiKanjiBot {Kanji}\' where {Kanji} is the one Kanji that you want the stroke order MP4 of ' + strDateTime
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

    strDateTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print 'Finished printMentionsTimeline with ' + str(len(statuses)) + ' statuses ' + strDateTime

def checkRunProgram():
    rtnBool = False
    try:
        with open('fixedConfig.json', 'r') as f:
            config = json.load(f)

        keepRunning = config['runProgram']
        if keepRunning == 'True':
            rtnBool = True
    except:
        print 'ERROR: cannot do checkRunProgram()'

    return rtnBool

def callTimer(secs):
    time.sleep(secs)
    return 1

def main():
    global intervalSeconds
    keepRunning = checkRunProgram()

    if keepRunning:
        # api = getAPI()
        api = getAPI2()

        # printHomeTimeline(api)

        # will overwrite everything with just this one setting
        # writeLastMentionID(datetime.datetime.now().strftime('%y%m%d%H%M%S'))

        # This didn't overwrite everything in there, but have to reformat the EOL
        # Also, if the field isn't there, it'll make one
        # updateLastMentionID(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

        while keepRunning:
            printMentionsTimeline(api)
            callTimer(intervalSeconds)
            keepRunning = checkRunProgram()

        print 'Done'
    else:
        print 'Exiting because keepRunning is False'

main()