# KanjiAliveMP4.py
# Sryn - 20181227

import urllib2
import unirest
import json

site = 'https://kanjialive-api.p.rapidapi.com/api/public/kanji/'

def rtnMP4Test(aChar):
    return 'rtnMP4Test ' + aChar

def getRapidAPIKey():
    with open('config.json', 'r') as f:
        config = json.load(f)

    return config['RapidAPI']['api-key']

def getResponse(aChar):
    kanjiCode = urllib2.quote(aChar.encode('utf-8'))
    url = site + kanjiCode
    RapidAPIKey = getRapidAPIKey()
    response = unirest.get(url,
        headers={
            "X-RapidAPI-Key": RapidAPIKey
        }
    )
    return response

# Assumes aChar isCJK
def getKanjiAliveMP4(aChar):
    try:
        response = getResponse(aChar)
    except:
        return 'ERROR: Cannot contact KanjiAlive thru RapidAPI successfully'

    try:
        responseDict = response.body
        mp4 = responseDict['kanji']['video']['mp4']
    except:
        mp4 = 'ERROR: Stroke Order MP4 for ' + aChar + ' not available from KanjiAlive'

    return mp4
