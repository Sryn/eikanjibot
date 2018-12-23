# Testing connectivity of this to kanjialive thru RapidAPI

import unirest
import config

kanjiCode = '%E8%B5%B7'

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