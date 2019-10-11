from fangolib import *
from time import sleep
import random

def Amazon():

    (w,h) = getScreenSize()

    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    launchActivity(*apps['Amazon'])
    pressKey(84)
    root = getXMLUI()
    textField = root.find(".//node[@resource-id='com.amazon.mShop.android.shopping:id/rs_search_src_text']")
    tap(*getCenter(textField))
    root = getXMLUI()
    clearSearch = root.find(".//node[@resource-id='com.amazon.mShop.android.shopping:id/rs_clear_text_button_accessibility']")
    
    if clearSearch != None:
        tap(*getCenter(clearSearch))
        print('clear text')
    
    insertText(random.choice(alphabet))
    insertText(random.choice(alphabet))
    sleep(1)
    clearSuggestion = root.findall(".//node[@resource-id='com.amazon.mShop.android.shopping:id/iss_search_dropdown_item_clear']")
    suggCount = len(clearSuggestion)
    print('previous Suggestions: {}'.format(suggCount))
    for i in range(suggCount):
        tap(*getCenter(clearSuggestion[0]))
        sleep(.2)   
    sleep(2)
    root = getXMLUI()
    suggNodes = root.findall(".//node[@resource-id='com.amazon.mShop.android.shopping:id/iss_search_dropdown_item_text']")
    suggestions = [suggNode.attrib['text'] for suggNode in suggNodes]
    if len(suggestions) > 0:
        suggestion = random.choice(suggestions)
        insertText(suggestion[2:])
        pressKey(66)
    
    sleep(3)
    swipe(w/2,h/2,w/2,0)
    sleep(1)
    tap(w/2,h/2)
    sleep(8)
