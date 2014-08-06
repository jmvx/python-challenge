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
    # 0,0 ... 99,0
    # 1,1 ... 98,1
    # 2,2 ... 97,2
    
    pink += colors[c:c+delta] # 98
    c = c+delta+1
    # 99,1 99,2 99,3 99,4 ... 99,99
    # 98,2 98,3           ... 98,98
    # 97,3                ... 97,97
    
    red += colors[c:c+delta] # 98
    c = c+delta+1
    delta = delta-1
    # 98,99 97,99 96,99 ... 0,99
    # 97,98 96,98 96,98 ... 1,98
    # 96,97             ... 2,97
    
    purple += colors[c:c+delta] # 97
    c = c+delta
    # 0,98 0,97 .... 0,1
    # 1,97 1,96 .... 1,2
    # 2,96      .... 2,3

p = 0
low = 0
high = 99
for y in range(50):

    for x in range(low, high):
        if p < len(green):
            new1.putpixel((x, y), green[p])
        if p < len(pink):
            new2.putpixel((x, y), pink[p])
        if p < len(red):
            new3.putpixel((x, y), red[p])
        if p < len(purple):
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
    



