
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
            
            rand = random.random()
            if rand < .5:
                Instagram(10)
            elif rand < .8:
                Amazon(10)
            else:
                print('sleep')
                pressKey(26)
                sleep(10)
                unlock(2001)            	
        except Exception as e:
            print(e)
            continue
			

