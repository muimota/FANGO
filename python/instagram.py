from fangolib import *
from time import sleep
import random
import uiautomator2 as ui2

def Instagram(loops = 1):

    (w,h) = getScreenSize()
    d = ui2.connect()
    
    for i in range(loops):

        buttons = []

        while buttons == [] :
            
            
            try:
                launchActivity(*apps['Instagram'])
            except:
                print('exception')
                pass
            root = getXMLUI(device=d)
            sleep(2)
            
            buttons = root.findall(".//node[@resource-id='com.instagram.android:id/tab_icon']")
            if buttons == []:
                print('no tab')
                continue
        
        tap(*getCenter(buttons[1]))
        sleep(.4)
        tap(*getCenter(buttons[1]))
        swipe(w/2,h/4,w/2,h/2)
        sleep(.7)
        #click in a random image from explore

        for i in range(random.randint(0,4)):
            swipe(w/2,3*h/4,w/2,h/4)

        root = getXMLUI(device=d)
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
            sleep(.5)
            root = getXMLUI(device=d)
            #detect if there is a multiple photograph
            multi = root.find(".//node[@resource-id='com.instagram.android:id/carousel_bumping_text_indicator']")
            if multi != None:
                print('multiimage')
                pages = int(multi.attrib['text'].split('/')[1])
                swipecoords = getCenter(multi)
                swipe(swipecoords[0],swipecoords[1],swipecoords[0],h/5,1000)
                
                for i in range(pages):
                    swipe(swipecoords[0],h/5,0,h/5,1000)
                    sleep(.5)
                root = getXMLUI(device=d)
            
            #detect hearts
            hearts = root.findall(".//node[@resource-id='com.instagram.android:id/row_feed_button_like']")
            if len(hearts) > 0:
                heart = random.choice(hearts)
                print('like!')
                tap(*getCenter(heart))
                sleep(.15)
                tap(*getCenter(heart))
            else:
                print('no hearts')
