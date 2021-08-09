from fangolib import *
from time import sleep
import random
import uiautomator2 as ui2

def Instagram(loops = 1):

    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    
    (w,h) = getScreenSize()
    d = ui2.connect()
    
    for i in range(loops):

        button = None
        print('launch Instagram')
   		
        try:
            launchActivity(*apps['Instagram'])
        except:
            print('exception')
            pass
        
        print('capture xml')

        

        #TODO:check is we are ina Comments page
        
        print("search")
        searchButton = ".//node[@content-desc='Search and Explore']"
        searchBox    = './/node[@resource-id="com.instagram.android:id/action_bar_search_edit_text"]'
        homeButton   = ".//node[@content-desc='Home'][@package='com.instagram.android']"
        searchSug    = './/node[@resource-id="com.instagram.android:id/row_hashtag_textview_tag_name"]'
        imgTile      = ".//node[@resource-id='com.instagram.android:id/image_button']"
        root = getXMLUI(device=d,selector=searchButton)
        searchBtn = root.find(searchButton)
        
        if searchBtn == None:

            print("search button not found")
            button = root.find(homeButton) 
            tap(*getCenter(button))
           
            root = getXMLUI(device=d,selector=searchButton)
            searchBtn = root.find(searchButton)
            
        if searchBtn:
            print("search button found")
        
        print("tap search")
        tap(*getCenter(searchBtn))
        
        #searchbox 
        
        root = getXMLUI(device=d,selector=searchBox)
        t = root.find(searchBox)
        
        
        if t == None:
            print("search box not found")
        
        tap(*getCenter(t))
        tap(*getCenter(t))
        

        insertText('#')
        insertText(random.choice(alphabet))
        insertText(random.choice(alphabet))
        sleep(1)
        swipe(w/2,h/2,w/2,h/6)
              
        #suggestion
        root = getXMLUI(device=d,selector=searchSug)
        suggestions = root.findall(searchSug)
        if not suggestions:
            print("suggestions not found")
        tap(*getCenter(random.choice(suggestions)))  	 
        #click in a random image from explore

        root = getXMLUI(device=d,selector=imgTile)
        sleep(random.randint(200,2000)/1000)
        for i in range(random.randint(1,4)):
            swipe(w/2,3*h/4,w/2,h/4,random.randint(500,1500)/1000)
            random.randint(500,1500)/1000

        sleep(random.randint(200,2000)/1000)

        root = getXMLUI(device=d,selector=imgTile)
        images = root.findall(imgTile)
        sleep(random.randint(1000,4000)/1000)
        print("found {} images".format(len(images)))

        clickableImages = [image for image in images if getCenter(image)[1] > h/5 or getCenter(image)[1] > 4*h/5]
        index = random.randint(0,len(clickableImages)-1)
        bounds = getCenter(clickableImages[index])
        
        print("{} images".format(len(clickableImages)))
        print("total:{} selected:{} bounds:{} desc:{}".format(len(clickableImages),index,bounds,clickableImages[index].attrib['content-desc']))
        tap(*bounds)
        print('feed')

        for i in range(random.randint(3,10)):
            
            random.randint(500,2000)/1000
            swipe(w/2,3*h/4,w/2,h/4,random.randint(300,1000))
           
            root = getXMLUI(device=d)
            #detect if there is a multiple photograph
            multi = root.find(".//node[@resource-id='com.instagram.android:id/carousel_index_indicator_text_view']")
            if multi != None:
                print('multiimage')
                pages = int(multi.attrib['text'].split('/')[1]) - 1
                swipecoords = getCenter(multi)
                swipe(swipecoords[0],swipecoords[1],swipecoords[0],h/5,1000)
                
                for i in range(pages):
                    swipe(swipecoords[0],h/5,0,h/5,1000)
                    sleep(.5)
                root = getXMLUI(device=d)
            
            #detect hearts
            hearts = root.findall(".//node[@resource-id='com.instagram.android:id/row_feed_button_like']")
            if len(hearts) > 0:
                if random.random() < 0.0005:
                    heart = random.choice(hearts)
                    print('like!')
                    tap(*getCenter(heart))
                    sleep(.15)
                    
            else:
                print('no hearts')
