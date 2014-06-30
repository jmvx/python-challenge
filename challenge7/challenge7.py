#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/def/oxygen.html

import Image

i = Image.open("oxygen-gray.png")
width, height = i.size

x = 1
while x < width:
    color = i.getpixel((x,0))
    print chr(color[0]),
    x = x+7

answer = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print "\n"
for i in answer:
    print chr(i),