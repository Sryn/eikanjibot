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
  * Get Twitter API Key for the Twitter Bot to use
* Test Twitter Bot to post MP4 or Animated GIF
  * Ensure posted MP4 or Animated GIF is played natively by Twitter
* Combine the Python program and Twitter Bot to work together
* Host the combined program Bot somewhere
  * Note on potential usage to gauge data requirements so as to anticipate data / hosting bill
  * Probably code in something into the Bot in case of cost overruns
  * Also think about and mitigate flooding
  * Build in telemetrics into the Bot for statistical purposes
* Release and announce the availability of the Bot