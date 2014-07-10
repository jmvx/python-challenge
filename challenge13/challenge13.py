#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/return/disproportional.html

import xmlrpclib

url = 'http://www.pythonchallenge.com/pc/phonebook.php'

server = xmlrpclib.Server(url)

print "METHODS:", server.system.listMethods(), "\n"

print "HELP/phone:", server.system.methodHelp("phone"), "\n"

print "PHONE NUMBER:", server.phone("Bert")

# curl http://huge:file@www.pythonchallenge.com/pc/return/evil4.jpg

# Bert is evil! go back!