
from time import sleep
from fangolib import *
from instagram import Instagram
from amazon import Amazon

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

            if isLocked():
                print('locked')
                unlock(2001)
                sleep(.5)
                if isLocked():
                    raise FangoException('imposible to unlock')
                else:
                    print('unlocked')
            
            #home
            pressKey(3)
            if random.random() < .3:
                Instagram(3)
            else:
                Amazon()
        except FangoException as e:
            print(e)
            continue

