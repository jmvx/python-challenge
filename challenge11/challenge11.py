#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/return/5808.html

import Image

im = Image.open("cave.png")
im.size
rgb = list(im.getdata())

im2 = Image.new("RGB",im.size,"white")
im2.putdata(rgb[::2])
im2.show()
        