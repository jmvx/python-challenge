#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/def/integrity.html

# un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

#first part is base 64
#second part is hex

username1 = ("B", "Z", "h", "9", "1", "A", "Y", "&", "S", "Y", "A")
username2 = ("af", "82", "00", "00", "01", "01", "80", "02", "c0", "02", "00", "00")

for y in username1:
    print ord(y),

print "\n"

for x in username2:
    print int(x,16),

