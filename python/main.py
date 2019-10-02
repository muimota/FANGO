
from time import sleep
from fangolib import *


def instagram(loops = 1):
    for i in range(loops):

        root = getXMLUI()

      
        launchActivity(*apps['Instagram'])
        buttons = root.findall(".//node[@resource-id='com.instagram.android:id/tab_icon']")
        tap(*extractBounds(buttons[1]))

        #click in a random image from explore

        for i in range(random.randint(1,4)):
            swipe(w/2,3*h/4,w/2,h/4)

        root = getXMLUI()
        imagesFrame = root.find(".//node[@class='android.widget.ListView'][@resource-id='android:id/list']")
        images = imagesFrame.findall(".//node[@class='android.widget.ImageView'][@resource-id='']")
        index = random.randint(4,len(images)-1)
        sleep(.5)
        bounds = extractBounds(images[index])

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
                tap(*extractBounds(heart))
                sleep(.15)
                tap(*extractBounds(heart))
            else:
                print('no hearts')
if __name__ == "__main__":

    if checkDevice():
        print('connected')
    else:
        print('disconnected')

    (w,h) = getScreenSize()

    print(isSuspended())
    unlock(2001)
    launchActivity(*apps['Instagram'])


