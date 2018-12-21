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
* Will have to host the Bot somewhere. The slackbot above is hosted at DigitalOcean using Docker.

Intended Usage Steps:

* Twitter User @aUser tweets '@eikanjibot 起'
* eikanjibot will reply back with '@aUser https://media.kanjialive.com/kanji_animations/kanji_mp4/o(kiru)_00.mp4'
* Or thru some other service / method that forces Twitter to show that MP4 file natively

To Do:

* Get Twitter handle @eikanji <- DONE
* Get associated URL <- DONE
* Point associated URL to @eikanji <- DONE but unconfirmed
* 

