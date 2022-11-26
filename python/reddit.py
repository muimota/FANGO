import fangolib as fl
from time import sleep
import random
import uiautomator2 as ui2

def Reddit(loops = 1):

    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    
    if not fl.packageInstalled(fl.apps['Reddit'][0]):
        return
    try:
        fl.sendAdb('am force-stop ' + fl.apps['Reddit'][0])
        fl.launchActivity(*fl.apps['Reddit'])
    except:
        print('exception')
        pass
    
    (w,h) = fl.getScreenSize()
    d = ui2.connect()

    selector = './/*[@resource-id="com.reddit.frontpage:id/link_list"]/node[@class="android.widget.LinearLayout"]'
    titles = './/*[@resource-id="com.reddit.frontpage:id/link_title"]'
    search_box = './/*[@resource-id="com.reddit.frontpage:id/feed_control_search_icon"]'
    search_results = './/*[@resource-id="com.reddit.frontpage:id/search_results"].//*[@class="android.widget.RelativeLayout"]'
    bottom_nav_btns = './/*[@resource-id="com.reddit.frontpage:id/bottom_nav"].//*[@class="android.view.ViewGroup"]'
    for i in range(loops):
        root = fl.getXMLUI(device=d,selector=bottom_nav_btns)
        home = root.findall(bottom_nav_btns)[0]
        fl.tap(*fl.getCenter(home))
        root = fl.getXMLUI(device=d,selector=search_box)
        fl.tap(*fl.getCenter(root.find(search_box)))
        fl.insertText("r/")
        #One letter to garantee we don't display any NSFW content
        fl.insertText(random.choice(alphabet)) 
        
        
        root = fl.getXMLUI(device=d,selector=search_results)
        results = root.findall(search_results)[:-1]
        
        for tries in range(3):
            
            root = fl.getXMLUI(device=d,selector=search_results)
            results = root.findall(search_results)[:-1]
        
            if len(results)== 0:
                print('empty results, giving a second chance')
                sleep(2)
            else:
                break

        fl.tap(*fl.getCenter(random.choice(results)))
        root = fl.getXMLUI(device=d,selector=titles)

        sleep(2)
        for i in range(random.randint(5,10)):
            
            fl.swipe(w/2,3*h/4,w/2,h/4,random.randint(300,1000))
            sleep(.5 + random.random() * 3.0)
    
    