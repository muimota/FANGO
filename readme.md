# FANGo

## Instagram

com.instagram.android:id/item_emoji
com.instagram.android:id/row_feed_emoji_picker_plus_icon

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

## ADB commands

reset server
adb kill-server&&adb start-server

get screen size
'''adb shell wm size'''
press power button 
'''adb shell input keyevent 26'''
list packages
'''adb shell pm list packages'''
visit url
'''adb shell am start -a android.intent.action.VIEW -d http://www.stackoverflow.com'''
launch Activity
'''adb shell am start -n com.instagram.android/com.instagram.mainactivity.MainActivity'''
show all activities from package [source](https://stackoverflow.com/a/51649936/2205297)
'''adb shell dumpsys package | grep -Eo "^[[:space:]]+[0-9a-f]+[[:space:]]+com.twitter.android/[^[:space:]]+" | grep -oE "[^[:space:]]+$"'''
check if it is locked  
'''adb shell dumpsys power | grep 'mHolding' '''  
dump interface [source](https://stackoverflow.com/a/39923793/2205297)
'''adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') view.xml'''
