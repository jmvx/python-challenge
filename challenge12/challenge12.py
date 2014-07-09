#!/usr/bin/env python

gfx = open('evil2.gfx','r')
data = gfx.read()

for i, extension in enumerate([ 'jpg', 'png', 'gif', 'png', 'jpg' ]):
    with open('output%i.%s' % (i, extension), 'w') as f:
      f.write(data[i::5])
  