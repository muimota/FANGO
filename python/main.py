
from time import sleep
from fangolib import *
from instagram import Instagram

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
                if isLocked():
                    raise Exception('imposible to unlock')
                else:
                    print('unlocked')
            
            Instagram(10)

        except FangoException as e:
            print(e)
            continue

