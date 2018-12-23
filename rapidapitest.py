#!/usr/bin/python
# coding: utf-8

# Line 2 tells the interpreter to treat the text in this file as unicode
# from https://www.python.org/dev/peps/pep-0263/

# Testing connectivity of this to kanjialive thru RapidAPI

import unirest
import config
import urllib2

# Have to tell the MS VS Code to accept the text below as unicode
# https://stackoverflow.com/q/24111955

# wake
wake = u'起'
wake_unicode = '%E8%B5%B7'
# cat
cat = u'猫'
cat_unicode = '%E7%8C%AB'

currentKanji = cat

# Convert the unicode to URL Escape Code
kanjiCode = urllib2.quote(currentKanji.encode('utf-8'))

def testRapidAPI():
    site = 'https://kanjialive-api.p.rapidapi.com/api/public/kanji/'
    url = site + kanjiCode
    response = unirest.get(url,
        headers={
            "X-RapidAPI-Key": config.RapidAPI['api-key']
        }
    )
    return response

def main():
    response = testRapidAPI()

    responseDict = response.body
    # https://stackoverflow.com/a/12934757
    mp4 = responseDict['kanji']['video']['mp4']

    print 'response.code = ' + str(response.code) + '\n'
    print 'response.headers:-\n' + str(response.headers) + '\n'
    # print 'response.body = ' + str(responseDict) + '\n'
    print 'mp4 = ' + mp4 + '\n'

main()