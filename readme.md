# FANGo
2019 - 2020 Martin Nadal
## Dependencies
 Some packages ([python3-pip](https://packages.debian.org/buster/python3-pip), [python3-lxml](https://packages.debian.org/buster/python3-lxml), [libopenjp2-7](https://packages.debian.org/buster/libopenjp2-7), [libtiff5](https://packages.debian.org/buster/libtiff5), [adb](https://packages.debian.org/buster/android-tools-adb)) are not installed by defult in **raspibian lite**
`apt install python3-pip python3-lxml libopenjp2-7 libtiff5 android-tools-adb`

it is necessary to restart the device once these packages are installed

python install [uiautimator2](https://pypi.org/project/uiautomator2/)
`pip3 install uiautomator2`

## development 

`interactive.py` is a script that declares and inits the libraries to make easier to work in iteractive mode use it `python -i interactive.py`

## Autostart
 fango.services can be installed as a service following this [tutorial](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

|action      | command                                                        |
|------------|---------------------------------------------------------|
|Install     |`sudo cp fango.service /etc/systemd/system`|
|start       |`sudo systemctl start fango.service`                  |
|stop        |`sudo systemctl stop fango.service`                  |
|enable at startup| `sudo systemctl enable fango.service`                |

# App Notes

This section has info abou the different applications

## Instagram

`com.instagram.android:id/item_emoji`
`com.instagram.android:id/row_feed_emoji_picker_plus_icon`
bottom buttons
`com.instagram.android:id/tab_icon`

## Youtube
like
com.google.android.youtube:id/like_button
like add
com.google.android.youtube:id/brand_interaction_thumbs_up

## Amazon
package:`com.amazon.mShop.android.shopping`
activity:`com.amazon.mShop.search.SearchActivity`

Pressing search button (84) opens search dialog
### resources-ids
search textfield
`com.amazon.mShop.android.shopping:id/rs_search_src_text`
clear search textfield
`com.amazon.mShop.android.shopping:id/rs_clear_text_button_accessibility`
clear search suggestion
`com.amazon.mShop.android.shopping:id/iss_search_dropdown_item_clear`

## Facebook

boton like:`text="Like"`
link compartido:`content-desc="Shared Link:  ... "`


## software

[python adb](https://github.com/google/python-adb)
[android-udev-rules](https://github.com/M0Rf30/android-udev-rules.git)

[Stanley](https://f-droid.org/en/packages/fr.xgouchet.packageexplorer/) an app to get Intent names from android apps.

## Cheatsheets

https://devhints.io/adb
https://infosecravindra.github.io/cheatsheets/adb-cheetsheet.html

extract UI to xml
https://stackoverflow.com/questions/26586685/is-there-a-way-to-get-current-activitys-layout-and-views-via-adb

In the future to control more than one device
https://developer.android.com/studio/command-line/adb#directingcommands

android keycodes
https://developer.android.com/reference/android/view/KeyEvent.html

## ADB commands

reset server
adb kill-server&&adb start-server

get screen size  
```adb shell wm size```  
press power button  
```adb shell input keyevent 26```  
list packages  
```adb shell pm list packages```  
visit url  
```adb shell am start -a android.intent.action.VIEW -d http://www.stackoverflow.com```  
launch Activity  
```adb shell am start -n com.instagram.android/com.instagram.mainactivity.MainActivity```  
show all activities from package [source](https://stackoverflow.com/a/51649936/2205297)  
```adb shell dumpsys package | grep -Eo "^[[:space:]]+[0-9a-f]+[[:space:]]+com.twitter.android/[^[:space:]]+" | grep -oE "[^[:space:]]+$"```  
check if it is locked  
```adb shell dumpsys power | grep 'mHolding' ```  
dump interface [source](https://stackoverflow.com/a/39923793/2205297)  
```adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') view.xml```  
