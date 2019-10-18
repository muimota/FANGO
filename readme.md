#FANGo

## Autostart
 fango.services can be installed as a service following this [tutorial](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

|            |                                                         |
|------------|---------------------------------------------------------|
|**Install** |`sudo cp fango.service /etc/systemd/system/fango.service`| 
|**start**   |`sudo systemctl start myscript.service`                  |
|**stop**    |`sudo systemctl start myscript.service`                  |
|**install** | `sudo systemctl enable myscript.service`                |
|            |                                                         |


## Instagram

`com.instagram.android:id/item_emoji`
`com.instagram.android:id/row_feed_emoji_picker_plus_icon`
botones de abajo
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
