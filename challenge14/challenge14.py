#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/return/italy.html

import Image

wire = Image.open("wire.jpg")
colors = list(wire.getdata())

new1 = Image.new("RGB", (100, 100), "white")
new2 = Image.new("RGB", (100, 100), "white")
new3 = Image.new("RGB", (100, 100), "white")
new4 = Image.new("RGB", (100, 100), "white")

width = 100
height = 100


green = []
pink = []
red = []
purple = []

delta = 99
c = 0
while delta > 0:
    green += colors[c:c+delta] # 99
    c = c+delta+1
    delta = delta-1
    
    pink += colors[c : c+delta] # 98
    c = c+delta+1
    
    red += colors[c:c+delta] # 98
    c = c+delta+1
    delta = delta-1
    
    purple += colors[c: c+delta] # 97
    c = c+delta

low = 0
high = 99
for y in range(50):
    p = 0
    for x in range(low, high):
        new1.putpixel((x, y), green[p])
        new2.putpixel((x, y), pink[p])
        new3.putpixel((x, y), red[p])
        new4.putpixel((x, y), purple[p])
    p = p+1
    low = low+1
    high = high-1
    if low == high or low > high:
        break

new2 = new2.rotate(270)
new3 = new3.rotate(180)
new4 = new4.rotate(90)

new1.show()
new2.show()
new3.show()
new4.show()


# 0,0 1,0 2,0 ... 97,0 98,0 99,0  # 0 - 99
#     1,1 2,1...  97,1 98,1       # 1 - 98
    



