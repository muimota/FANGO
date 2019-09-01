import os
import re
from time import sleep
import xml.etree.ElementTree as ET
import random

apps = {'GoogleMaps':('com.google.android.apps.maps','com.google.android.maps.MapsActivity'),
		'Instagram':('com.instagram.android','com.instagram.mainactivity.MainActivity')}

def checkDevice():
    """checks if device is open"""
    output   = os.popen('adb devices').read()
    devices = [line for line in output.split('\n') if len(line.strip()) > 0][1:]
    
    return len(devices) > 0

def sendAdb( command, debug = False ):
    """send a adb shell command"""
    if debug:
        print('adb shell {}'.format(command))
    
    return os.popen('adb shell {}'.format(command)).read()

def pressKey(keyCode):
    """send a key press can be a character or a phone's button"""
    return sendAdb('input keyevent {}'.format(keyCode))

def insertText(text):
    """insert text as if it was inserted from an external keyboard"""
    sendAdb('input  keyboard text \"{}\"'.format(text))

def getScreenSize():
    """return screen size in a tuple"""
    output  = sendAdb('wm size')
    m = re.search(r'.*:\s+([0-9]+)x([0-9]+)', output)
    return (int(m.group(1)), int(m.group(2)))

def getXMLUI():
    """get the UI in XML format"""
    output  = sendAdb('uiautomator dump')

    m = re.search(r'(\S+.xml)', output)
    if m == None:
        print('error')
        filepath = '/sdcard/window_dump.xml'
    else:
        filepath = m.group(1)
    xmlstr = sendAdb('cat {}'.format(filepath))
    root = ET.fromstring(xmlstr)
    return root

def extractBounds(xmlElement):
    
    bounds = xmlElement.attrib['bounds']
    print(bounds)
    m = re.search(r'\[([0-9]+),([0-9]+)\]',bounds)
    return (int(m.group(1)) + 5,int(m.group(2)) + 5)


def openURL(url):
	"""open URL with the default browser"""
	sendAdb( 'am start -a android.intent.action.VIEW -d {}'.format(url))

def launchActivity(package,intent):
	"""Launch an Activity from a package"""
	sendAdb( 'am start -n {}/{}'.format(package,intent))

def swipe(x0,y0,x1,y1, ms = 500 ):
	"""send swipe start, end coordinates and miliseconds"""
	sendAdb('input swipe {} {} {} {} {}'.format(x0,y0,x1,y1,ms))

def tap(x,y,ms = 0):
    """tap the screen"""
    if ms > 0:
        swipe(*((x,y) + (x,y) + (ms,)))
    else:
        sendAdb( 'input tap {} {}'.format(x,y))

def getDump(subsytem,term = None):
	"""retrieves sysdump of a system optionally can filter the output"""
	lines = sendAdb('dumpsys {}'.format(subsytem)).split('\n')
	if term != None:
		lines = list(filter(lambda l:term in l,lines))
	return lines



def isSuspended():
	"""Check if it is suspended (black screen)"""
	return getDump('power','mHoldingDisplaySuspendBlocker=true')==[]

def isLocked():
	"""Check if it is locked"""
	return getDump('power','mUserActivityTimeoutOverrideFromWindowManager=-1')==[]

def unlock(PIN = None):
    """unlock phone, swipes from bottom to the middle of the screen + PIN + enter"""
    pressKey(26)
    sleep(1)
    if isSuspended():
        pressKey(26)
    (w,h) = getScreenSize()  
    swipe(w/2,h/2,w/2,0)
    if PIN != None:
        insertText(PIN)
        pressKey(66)

if __name__ == "__main__":
	
    import time
    
    if checkDevice():
        print('connected')
    else:
        print('disconnected')
    
    (w,h) = getScreenSize()  

    print(isSuspended())
    unlock(2001)
    launchActivity(*apps['Instagram'])
    
    
   
    
    for i in range(50):

        root = getXMLUI()

        #explore
        #buttons = root.findall(".//node[@resource-id='com.instagram.android:id/tab_icon']")
        #if len(buttons) ==  0:
        #pressKey(3) #home
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
        sleep(1)
        bounds = extractBounds(images[index])
        
        print("total:{} selected:{} bounds:{} desc:{}".format(len(images),index,bounds,images[index].attrib['content-desc']))
        tap(*bounds)
        print('feed')
        
        for i in range(2):
        
            swipe(w/2,3*h/4,w/2,h/4)
            sleep(.5)
            root = getXMLUI()
            hearts = root.findall(".//node[@resource-id='com.instagram.android:id/row_feed_button_like']")
            if len(hearts) > 0:
                heart = random.choice(hearts)
                tap(*extractBounds(heart))
                sleep(.5)
                tap(*extractBounds(heart))
            else:
                print('no hearts')
