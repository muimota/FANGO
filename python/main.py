import os
import re
from time import sleep

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
    sendAdb('input  keyboard text \"{}\"'.format(text),True)

def getScreenSize():
    """return screen size in a tuple"""
    output  = sendAdb('wm size')
    m = re.search(r'.*:\s+([0-9]+)x([0-9]+)', output)
    return (int(m.group(1)), int(m.group(2)))

def openURL(url):
	"""open URL with the default browser"""
	sendAdb( 'am start -a android.intent.action.VIEW -d {}'.format(url))

def launchActivity(package,intent):
	"""Launch an Activity from a package"""
	sendAdb( 'am start -n {}/{}'.format(package,intent))

def swipe(x0,y0,x1,y1):
	"""send swipe"""
	sendAdb('input swipe {} {} {} {}'.format(x0,y0,x1,y1))

def tap(x,y):
    """tap the screen"""
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
    sleep(0.500)
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
    print(isLocked())
    unlock()
