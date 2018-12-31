# eikanjibot
A Twitter Bot that replies with an mp4 file of the kanji's stroke order.

Intention:
* Use Python
* Build Twitter Bot
* Will probably base on this project:
  * https://www.dataquest.io/blog/apartment-finding-slackbot/
  * https://github.com/VikParuchuri/apartment-finder
* Will probably use the KanjiAlive API:
  * https://kanjialive.com/
  * https://app.kanjialive.com/api/docs
* Whose API is currently hosted via RapidAPI:
  * https://rapidapi.com/KanjiAlive/api/learn-to-read-and-write-japanese-kanji
* Will have to get a good Make Twitter Bot tutorial.
* Will have to host the Bot somewhere. The slackbot above is hosted at DigitalOcean using Docker.

Intended Usage Steps:
* Twitter User @aUser tweets '@eikanjibot 起'
* eikanjibot will reply back with '@aUser https://media.kanjialive.com/kanji_animations/kanji_mp4/o(kiru)_00.mp4'
* Or thru some other service / method that forces Twitter to show that MP4 file natively

To Do:
* Get Twitter handle @eikanjibot <- DONE
* Get associated URL <- DONE
* Point associated URL to @eikanjibot <- DONE <strike>but unconfirmed</strike>
* Make a Python program to call the kanjialive API
  * Get a RapidAPI Key <- DONE
    * rudimentary program w/ unirest working OK
  * Need to learn to use Python's JSON style to get specific field in response body <- https://stackoverflow.com/a/12934757
  * Need to learn how to obfuscate the RapidAPI Key from the code
    * https://martin-thoma.com/configuration-files-in-python/
    * http://www.blacktechdiva.com/hide-api-keys/ for the .gitignore
    * Need to change RapidAPI Key now <- Done - Just made a new project in RapidAPI
  * Need to investigate the kanji code the kanjialive API accepts
    * Have to tell the Python 2.7 interpreter to treat the text in the file as unicode <- https://www.python.org/dev/peps/pep-0263/
    * Also have to tell MS VS Code to accept the kanji text as unicode and also to convert the kanji unicode to URL Escape Code to be used in the KanjiAlive API <- https://stackoverflow.com/q/24111955
  * Also need to think about error possibilities and implement error mitigating code
  * KanjiAlive returns link to associated MP4. Have to think about how to post for Twitter to play that MP4 natively.
      * Twitter only allows direct MP4 uploads from user's / bot's file system, so can't use KanjiAlive MP4 URL to upload.
      * Thinking of ways around this:
        1. Pre-upload the MP4, and then refer to that tweet whenever a user ask's for a specific kanji's stroke order
  * For now, just post the kanji's animated stroke order using MP4
  * Later on might look into Animated GIFs (? - Not sure if this is better)
  * Might want to think ahead into future versions where:
    * The kanji data is hosted ourselves
    * For kanji whose stroke order MP4 isn't available, might want to look into automatically converting static pics of stroke order into animated GIFs
* Make Twitter Bot
  * Get Twitter API Key for the Twitter Bot to use <- DONE for Twitter eiKanjiBot App
  * Create test eiKanjiBot Twitter App
    * DONE - using https://tweepy.readthedocs.io/en/3.7.0/getting_started.html
    * Also proved ability to post tweet - using https://www.twilio.com/blog/build-deploy-twitter-bots-python-tweepy-pythonanywhere
  * Should test ability to detect query tweet and reply to that tweet
    * Used:
      * http://docs.tweepy.org/en/3.7.0/api.html
      * https://developer.twitter.com/en/docs/tweets/timelines/api-reference/get-statuses-home_timeline
    * Detect query tweet
      * DONE - detected mention tweet
      * Test detect only mention tweets since last previous replied mention tweet <- DONE
      * Should store the tweet ID of the last mention that was replied to in the filesystem (config.py?)
        * DONE - using ConfigParser + JSON
        * based on https://stackoverflow.com/a/19078712
    * Reply to that tweet
      * DONE and verified
      * Issue now is that getting mentions again would receive a list of mentions that include the previous replied to mention and that mention is (might be) at the end of the list. So updating lastMentionID could actually start at the newest mention and then ignore all other mentions between that and the previous replied to mention.
        * Fixed this by only getting statuses (mentions) that are newer than lastMentionID
      * Now, have to ensure that the lastMentionID that is updated in config.json is the newest of the statuses 
        * Done this by moving the updateLastMentionID to the function that gets the mentions and only updating the largest number status.id
  * Need to prepare some draft functions that:
    1. Reads the body of the query tweet/mention/status <- DONE
    2. Remove the '@aTwitterUser ' from it, where that is the Twitter handle of the user that sent the mention + the space after it <- DONE
    3. Gets the first character of the remaining body
       * DONE - but might need to make a more robust function
       * I think I made a more robust function for this by trimming
         * https://stackoverflow.com/a/663175
         * https://stackoverflow.com/a/1185529
    * Have to code how to determine a character is a (Japanese) kanji
      * https://docs.python.org/2/library/unicodedata.html
      * using 'import unicodedata'
      * get character's name
      * check if character's name starts with 'CJK'
      * Note: Can't differentiate if Chinese, Japanese or Korean 'Han' character as Unicode is a unified character set for East Asian characters
    4. Determines whether that character is a (Japanese) kanji or not
       * If that is not a (Japanese) kanji, then reply to @aTwitterUser that it (the bot) cannot understand the query mention and include a usage message, or don't reply at all, or ..
       * If that is a (Japanese) kanji, then reply back to @aTwitterUser that same kanji
      * DONE - For now, reply with usage help to non-kanji mentions
* Test Twitter Bot to post MP4 or Animated GIF
  * Need to call up the other Python file to get the stroke order MP4 (? Should I do it this way)
    * DONE - Figured out it was something similar to the config.py settings import, but this time a function call
  * Ensure posted MP4 or Animated GIF is played natively by Twitter
    * Skipping this for this version
* Combine the Python program and Twitter Bot to work together
  * DONE - For now, it is not very self error correction
  * Need to list dependencies and code error mitigation
  * Need to code in periodic check of @eiKanjiBot received mentions every 15 secs (?)
    * DONE - see setIntervalTest.py
  * Have set an on/off switch in the runProgram field in fixedConfig.json
  * Moved lastMentionID field to varConfig.json
  * config.json is now purely for secret settings
* Host the combined program Bot somewhere
  * Note on potential usage to gauge data requirements so as to anticipate data / hosting bill
  * Probably code in something into the Bot in case of cost overruns
  * Also think about and mitigate flooding
  * Build in telemetrics into the Bot for statistical purposes
* Make config.json.example
* Release and announce the availability of the Bot
  * It's Alive!!
    * Hosted on @PythonAnywhere
      * Running it in the background
      * https://stackoverflow.com/questions/2975624/how-to-run-a-python-script-in-the-background-even-after-i-logout-ssh
      * Had to comment out two print lines that also prints the kanji, as the bash console on PA can't show unicodes outside a certain range
      * Also had to comment out the 'import config' + getAPI() as I didn't upload config.py
    * Announced on Twitter and Reddit at about 5:45pm Fri 28th Dec 2018, UTC+8
    * Got twitter banned twice because update testing caused spamming. Fixed those errors and hope Twitter lifts the ban.