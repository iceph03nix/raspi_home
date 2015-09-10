#import modules
from datetime import datetime
from time import sleep
from pytz import timezone


#set CONSTANTS
TIME_ZONE = timezone('US/Central')
START_TIME = datetime.strptime('1555','%H%M').time()                  #enter the time of day to begin the cycle
RUN_TIME = 1                           #enter the length of time to run each zone in minutes
TOTAL_ZONES = 4                         #enter the number of zones you have, zones will$
DAYS = [0, 1, 2, 3, 4, 5, 6]            #select days of week to run as list, 0 for sund$
TEST_MODE = True                        #set true to print pinouts and duration instead of activating GPIO
PIN_LIST = [3, 5, 7, 8]

#set initialVariables
rtSeconds = RUN_TIME*60
day = datetime.now(TIME_ZONE)
currentDay = day.weekday()
currentTime = day.time().replace(second=0, microsecond=0)

#setup GPIO

#Functions
def activatePin(pin, duration):
    if TEST_MODE == True:
        print(pin, )
        print(duration, )
        print(currentDay, )
        print(datetime.now(TIME_ZONE).time())
        sleep(duration)
    else:
        sleep(duration)

def convertTime(time):                  #convert times back to datetime so it can be compared (because python can be stupid sometimes)
    conTime = datetime.now().replace(hour=time.hour, minute=time.minute)
    return conTime


def offTimeDebug():
    print('Next Scheduled watering: ',' ')
    if currentTime < START_TIME:
        waitTime = convertTime(START_TIME) - convertTime(currentTime)
        print(datetime.strftime(waitTime))
        if waitTime.total_seconds() > 330:
            sleep(300)
        else:
            sleep(30)
    else:
        print('Tomorrow')
        sleep(3600)
        


#Main Program
while True:
    day = datetime.now(TIME_ZONE)
    currentDay = day.weekday()
    currentTime = day.time().replace(second=0, microsecond=0)

    if currentDay in DAYS:               #check to make sure it's the right day to water
        if currentTime == START_TIME:
            for zone in range(TOTAL_ZONES):
                activatePin(PIN_LIST[zone],rtSeconds)
        else:
            offTimeDebug()
            #print(currentTime, )
            #print('Not the right time')
            #sleep(1)

