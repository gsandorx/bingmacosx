#!/usr/bin/python
#
# Download Bing's picture of the day and set it as your desktop background
#
# OS: Mavericks and newer versions of OSX
# 
# Sandor Gonzalez 
# gsandorx - at - gsandorx - dot - com 
#
# 2016
#

import urllib2
import json
import subprocess
import os
import os.path

bingURL = 'http://bing.com'
imgJsonPath = '/HPImageArchive.aspx?format=js&idx=0&n=1'
imgJsonURL = bingURL + imgJsonPath

picturesLibPath = os.getenv("HOME") + '/Pictures/Bing'

if not os.path.exists(picturesLibPath):
	os.makedirs(picturesLibPath)


# Load Bing JSON content and extract the image URL

jsonRaw = urllib2.urlopen(imgJsonURL)
jsonData = json.load(jsonRaw)
imgURL = bingURL + jsonData['images'][0]['url']

# Save the image to a file

imgRaw = urllib2.urlopen(imgURL)
imgFileName = picturesLibPath + '/' + imgURL.split('/')[-1]

img = open(imgFileName, 'w')
img.write(imgRaw.read())
img.close()

# Set the new image as Desktop background using Apple's script
#  osascript -e "tell application \"System Events\" to set picture of every desktop to \"/path/to/image.jpg\""

subprocess.check_call(["/usr/bin/osascript", "-e", "tell application \"System Events\" to set picture of every desktop to \"%s\""%imgFileName])
