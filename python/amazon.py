from fangolib import *
from time import sleep
import random
import uiautomator2 as ui2
import glob
import re
def Amazon(loops = 6,savescreens = False):
    
    (w,h) = getScreenSize()
    d = ui2.connect()
    images = sorted(glob.glob('screens/*.png'))
    
    if len(images) > 0:
        lastimage = images[-1]
        imageIndex = int(re.match(r'.*/([0-9]+)\.png',lastimage).group(1))
    else:
        imageIndex = 0
    try:
        launchActivity(*apps['Amazon'])
        skip_login = root.find(".//node[@resource-id='com.amazon.mShop.android.shopping:id/skip_sign_in_button']")
        if skip_login :
        	 tap(*getCenter(skip_login))	
    except:
        print('oh!')
        pass

    for i in range(loops):
        alphabet = ('abcdefghijklmnopqrstuvwxyz')
        
        pressKey(84)
        root = getXMLUI(device = d)
        textField = root.find(".//node[@resource-id='com.amazon.mShop.android.shopping:id/rs_search_src_text']")
        tap(*getCenter(textField))
        root = getXMLUI(device = d)
        clearSearch = root.find(".//node[@resource-id='com.amazon.mShop.android.shopping:id/rs_clear_text_button_accessibility']")
        
        if clearSearch != None:
            tap(*getCenter(clearSearch))
            print('clear text')
        
        insertText(random.choice(alphabet))
        insertText(random.choice(alphabet))
        #insertText('er')
        
        sleep(.2)
        root = getXMLUI(device = d)
        clearSuggestion = root.findall(".//node[@resource-id='com.amazon.mShop.android.shopping:id/iss_search_dropdown_item_clear']")
        suggCount = len(clearSuggestion)
        print('previous Suggestions: {}'.format(suggCount))
        sleep(1)
        for i in range(suggCount):
            tap(*getCenter(clearSuggestion[0]))
            sleep(.2)   
        sleep(1)
        
        root = getXMLUI(device = d)
        suggNodes = root.findall(".//node[@resource-id='com.amazon.mShop.android.shopping:id/iss_search_dropdown_item_text']")
        suggestions = [suggNode.attrib['text'] for suggNode in suggNodes]
        print(suggestions)
        if len(suggestions) > 0:
            suggestion = random.choice(suggestions)
            print(suggestion)
            insertText(suggestion[2:])
            sleep(1)
            pressKey(66)
            
        sleep(2)
        swipe(w/2,h/2,w/2,0,random.randint(300,600))
        sleep(1)
        root = getXMLUI(device = d)
        views = root.findall(".//node[@class='android.view.View']")
        products = [view for view in views if len(view.attrib['text'].strip()) > 0 ]
        if len(products) > 0:
            product = random.choice(products)
            print('product:{}'.format(product.attrib['text']))
            tap(*getCenter(product))
        else:
            print('no product found, tap in center')
            tap(w/2,h/2)
            
        sleep(6)
        imageIndex += 1
        filename = 'screens/{:06}.png'.format(imageIndex)
        if savescreens == True:
        	screenshot(filename)
        	print('save screenshot:{}'.format(filename))
        #multi image
        root = getXMLUI(device = d)
        pagination_block = root.find(".//node[@resource-id='image-block-pagination-dots']")
        if pagination_block != None:
            pages_count = max([int(node.attrib['index']) for node in pagination_block.iter()])
            image_block = root.find(".//node[@resource-id='image-block-row']")
            centerImage = getCenter(image_block)
            for i in range(pages_count - 1):
                swipe(centerImage[0] + w/4 ,centerImage[1],centerImage[0] -  + w/4 ,centerImage[1])
                sleep(1)
            

        
        
