# FANGoLib
# 2019 Martin Nadal martin@muimota.net

from subprocess import PIPE, Popen
import re
from time import sleep
import xml.etree.ElementTree as ET
import random

apps = {'GoogleMaps':('com.google.android.apps.maps','com.google.android.maps.MapsActivity'),
		'Instagram':('com.instagram.android','com.instagram.mainactivity.MainActivity'),
        'Amazon':('com.amazon.mShop.android.shopping','com.amazon.mShop.splashscreen.StartupActivity')
        }

class FangoException(Exception):
    pass

def checkDevice():
    """checks if device is open"""
    p = Popen('adb devices', shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate() 
    output = stdout.decode('utf-8')
    devices = [line for line in output.split('\n') if len(line.strip()) > 0][1:]

    return len(devices) > 0


def sendAdb( command, debug = False, binary = False):
    """send a adb shell command"""
    adbCommand = 'adb shell {}'.format(command)
    p = Popen(adbCommand, shell=True, stdout=PIPE, stderr=PIPE)
    
    stdout, stderr = p.communicate()
    
    if debug:
        print(adbCommand)
        print(stderr)

    if b'error: no devices/emulators found' in stderr:
        raise FangoException('No device/emulator found')
    if b'Warning: Activity not started, intent has been delivered to currently running top-most instance.' in stderr:
        raise FangoException('activity not started')
    
    if binary:
        return stdout
    else:
        return stdout.decode('utf-8')



def pressKey(keyCode):
    """send a key press can be a character or a phone's button"""
    return sendAdb('input keyevent {}'.format(keyCode))

def insertText(text):
    """insert text as if it was inserted from an external keyboard"""
    sendAdb('input  text \\"{}\\"'.format(text))

def getScreenSize():
    """return screen size in a tuple"""
    output  = sendAdb('wm size')
    m = re.search(r'.*:\s+([0-9]+)x([0-9]+)', output)
    return (int(m.group(1)), int(m.group(2)))

def getXMLUI(filename = None,device = None):
    """get the UI in XML format"""
    if device == None:
        output  = sendAdb('uiautomator dump')
        m = re.search(r'(\S+.xml)', output)
        if m == None:
            print('no xml')
            filepath = '/sdcard/window_dump.xml'
        else:
            filepath = m.group(1)

        xmlstr = sendAdb('cat {}'.format(filepath))
    else:
        try:
            xmlstr = device.dump_hierarchy()
        except :
            raise FangoException('UIAutomator2 exception')
        
    root = ET.fromstring(xmlstr)
    if filename != None:
        ET.ElementTree(root).write(filename)
    return root

def getBounds(xmlElement):
    """returns press coords from an UI element"""
    bounds = xmlElement.attrib['bounds']
    m = re.search(r'\[([0-9]+),([0-9]+)\]\[([0-9]+),([0-9]+)\]',bounds)
    return (int(m.group(1)),int(m.group(2)),int(m.group(3)),int(m.group(4)))

def getCenter(xmlElement):
    """returns press coords from an UI element"""
    bounds = getBounds(xmlElement)
    return (( bounds[0] + bounds[2]) // 2, (bounds[1] + bounds[3]) // 2)

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

def screenshot(filename):
    img = sendAdb('screencap -p',binary=True)
    #https://blog.shvetsov.com/2013/02/grab-android-screenshot-to-computer-via.html
    #img = img.replace(b'\r\n',b'\n')
    with open(filename,'wb') as f:
        f.write(img)

def getContainers(x,y,xmlElements):
    """get nodes that contains certain coordinates x,y usefull to find elements"""
    filtered = []
    for node in nodes:
        bounds = getBounds(node)
        if bounds[0] < x and bounds[2] > x and bounds[1] < y and bounds[3] > y:
            filtered.append(node)
    return filtered

def getBatteryLevel():
    """reads phones battery level"""
    #https://www.programmersought.com/article/38291685131/
    battStatus = sendAdb("dumpsys battery")
    battDict = {}
    battFields =  [[fieldPair.strip() for fieldPair in line.split(':')] for line in battStatus.split('\n')] 
    battFields = [pairs for pairs in battFields if (len(pairs) > 1 and len(pairs[1]) > 1)]
    battDict = dict(battFields)
    
    return int(battDict['level'])

def setScreenBrightness(level):
    """sets screens brightness 0-255"""
    sendAdb("settings put system screen_brightness {}".format(level))

def packageInstalled(packageName):
    """checks if a package is installed"""
    packageName = packageName.strip()
    packageStatus = sendAdb('pm list packages {} '.format(packageName))
    return packageName in packageStatus
