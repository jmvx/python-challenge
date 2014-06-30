#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib2

response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')

while True:
    html = response.read()
    print "contents: " + html
    blah = html.split(' ')
    if str(blah[len(blah)-1]) == 'peak.html':
        print "Found answer"
        break
    if str(blah[len(blah)-1]) == 'going.':
        old_url = response.geturl()
        segments = old_url.rpartition('=')
        nothing = str(int(segments[2]) / 2)
        new_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + nothing
        print "new url ending: " + nothing
    else:
        new_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(blah[len(blah)-1])
        print "new url ending: " + str(blah[len(blah)-1])
    response = urllib2.urlopen(new_url)
