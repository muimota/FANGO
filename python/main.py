
from time import sleep
from fangolib import *
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

            rand = random.random()

            if rand < .33:
                Instagram(5)
            elif rand < .66:
                Amazon(10)
            else:
                Reddit(10)

        except Exception as e:
            print(e)
            continue
