
from time import sleep
from fangolib import *
import uiautomator2 as ui2
from instagram import Instagram
from amazon import Amazon
from reddit import Reddit

if __name__ == "__main__":

    while True:
        try:
            if checkDevice() == False:
                print('not connected')
                sleep(5)
                continue
            else:
                print('connected')

            (w,h) = getScreenSize()

            level = getBatteryLevel()
            print("battery level:{}".format(level))
            if level < 30:
                setScreenBrightness(min(level,30))
            elif level < 60:
                setScreenBrightness(min(level,128))


            if isLocked():
                print('locked')
                unlock(2001)
                sleep(.5)
                if isLocked():
                    raise FangoException('impossible to unlock')
                else:
                    print('unlocked')

            
            #there is a chance that running app returns null
            runningApp = getRunningActivity()
            
            if runningApp:
                (package,activity) = runningApp
                print('running {}/{}'.format(package,activity))
                if 'net.muimota' in package:
                    sleep(20)
                    continue

            #home
            pressKey(3)

            rand = random.random()

            if rand < .33:
                Instagram(10)
            elif rand < .66:
                Amazon(10)
            else:
                Reddit(10)

            
            
        except Exception as e:
            print(e)
            sleep(1)
            continue

        
