# bingmacosx
Pyhon script to sets Bing's daily image as your Mac OS X desktop background.

The script is supposed to be run either manually or through a scheduled task. 

Main script name: bing.py

I have included a the launchd plist file that I used on my own computer to setup a task to run this script. Just copy this file to ~/Library/LaunchAgents, edit the file to point to your script location, adjust the schedule and run the command below to load the new launchd agent:

launchctl load -w ~/Library/LaunchAgents/com.gsandorx.bingmacosx.plist 
