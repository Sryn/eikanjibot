# setIntervalTest.py
# 20181228 - Sryn
# Testing the ability to do something periodically <- Proven
# Although, StackOverflow guys mentioned something about time drift
# I think a time drifting correction code can be implemented, but it is not implemented here

import time
import datetime

stillProcessing = False
maxLoopCount = 10
intervalSeconds = 5.0

def callTimer(secs):
    time.sleep(secs)
    return 1

def main():
    global stillProcessing
    global maxLoopCount
    global intervalSeconds

    stillProcessing = True
    i = 0
    while stillProcessing:
        strDateTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        print 'i = ' + str(i) + ' \t' + strDateTime
        if i < maxLoopCount:
            i += callTimer(intervalSeconds)
        else:
            stillProcessing = False

main()