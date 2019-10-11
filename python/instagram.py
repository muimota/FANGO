from fangolib import *
from time import sleep
import random

def Instagram(loops = 1):

    (w,h) = getScreenSize()
    
    for i in range(loops):

        buttons = []

        while buttons == [] :
            root = getXMLUI()
            try:
                launchActivity(*apps['Instagram'])
            except:
                pass
            
            buttons = root.findall(".//node[@resource-id='com.instagram.android:id/tab_icon']")
            if buttons == []:
                pressKey(4)
        
        tap(*getCenter(buttons[1]))

        #click in a random image from explore

        for i in range(random.randint(1,4)):
            swipe(w/2,3*h/4,w/2,h/4)

        root = getXMLUI()
        images = root.findall(".//node[@class='android.widget.ImageView'][@resource-id='com.instagram.android:id/image_button']")
        index = random.randint(0,len(images)-1)
        index = 0
        #sleep(.5)
        clickableImages = [image for image in images if getCenter(image)[1] > h/5 or getCenter(image)[1] > 4*h/5]
        bounds = getCenter(clickableImages[index])

        print("total:{} selected:{} bounds:{} desc:{}".format(len(images),index,bounds,images[index].attrib['content-desc']))
        tap(*bounds)
        print('feed')

        for i in range(random.randint(1,10)):

            swipe(w/2,3*h/4,w/2,h/4,random.randint(300,1000))
            
            root = getXMLUI()
            hearts = root.findall(".//node[@resource-id='com.instagram.android:id/row_feed_button_like']")
            if len(hearts) > 0:
                heart = random.choice(hearts)
                tap(*getCenter(heart))
                sleep(.15)
                tap(*getCenter(heart))
            else:
                print('no hearts')