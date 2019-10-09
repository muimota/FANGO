
from time import sleep
from fangolib import *


def instagram(loops = 1):
    for i in range(loops):

        buttons = []

        while buttons == [] :
            root = getXMLUI()
            try:
                launchActivity(*apps['Instagram'])
            except:
                pass
            resource-id="com.instagram.android:id/tab_bar"
            buttons = root.findall(".//node[@resource-id='com.instagram.android:id/tab_icon']")
            if buttons == []:
                pressKey(4)
        
        tap(*getCenter(buttons[1]))

        #click in a random image from explore

        for i in range(random.randint(1,4)):
            swipe(w/2,3*h/4,w/2,h/4)

        root = getXMLUI()
        imagesFrame = root.find(".//node[@class='android.widget.ListView'][@resource-id='android:id/list']")
        images = imagesFrame.findall(".//node[@class='android.widget.ImageView'][@resource-id='']")
        index = random.randint(4,len(images)-1)
        sleep(.5)
        bounds = getCenter(images[index])

        print("total:{} selected:{} bounds:{} desc:{}".format(len(images),index,bounds,images[index].attrib['content-desc']))
        tap(*bounds)
        print('feed')

        for i in range(10):

            swipe(w/2,3*h/4,w/2,h/4)
            sleep(.15)
            root = getXMLUI()
            hearts = root.findall(".//node[@resource-id='com.instagram.android:id/row_feed_button_like']")
            if len(hearts) > 0 and random.random() < .2:
                heart = random.choice(hearts)
                tap(*getCenter(heart))
                sleep(.15)
                tap(*getCenter(heart))
            else:
                print('no hearts')
if __name__ == "__main__":

    while True:
        try:
            if checkDevice() == False:
                print('not connected')
                sleep(5)
                continue

            (w,h) = getScreenSize()

            if isSuspended():
                unlock(2001)
                if isSuspended():
                    raise Exception('imposible to unlock')

            instagram()

        except FangoException as e:
            print(e)
            continue

