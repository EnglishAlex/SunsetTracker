#!/usr/bin/env python

import sys
import inkyphat
import time
from PIL import ImageFont
from datetime import datetime

today = datetime.today()
KIWLdate = datetime(2018, 6, 13,8,0)
delta = KIWLdate - today

#print(KIWLdate, today)
#print(delta.days)
#print(delta.seconds)
#print(datetime.today().replace(microsecond=0))
#print(datetime.today())
#print("hours to KIWL - " + str(int(delta.total_seconds()/60/60)))


delta = KIWLdate - today

font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 22)

line1  = "KIWL 2018 in : "
line2  = str(delta.days) + " days"
# hours to KIWL start 8am June 13
line3  = str(int(delta.total_seconds()/3600)) + " hours"
timeNow = time.strftime("%H:%M")

# add some lines to make it look good
inkyphat.text((6, 6), line1, inkyphat.BLACK, font)
inkyphat.line((3,30,206,30), fill = True )
inkyphat.text((6,32), line2, inkyphat.RED  , font)
inkyphat.line((3,60,206,60), fill = True)
inkyphat.text((6,62), line3, inkyphat.RED  , font)

font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 14)
inkyphat.text((170,90), timeNow ,  inkyphat.BLACK, font)

inkyphat.show()

