#!/usr/bin/env python

import zipfile

z = zipfile.ZipFile("channel.zip","r")
info = z.infolist()
names = z.namelist()

file = open('/Users/julia/Google Drive/Projects/pythonchallenge/challenge6/channel/90052.txt','r')
    
while True:
    contents = file.readlines()
    for line in contents:
        pieces = line.split(' ')
    
    newloc = pieces[len(pieces)-1]
    filename = "/Users/julia/Google Drive/Projects/pythonchallenge/challenge6/channel/" + newloc + ".txt"
    
    for n in names:
        if n == (newloc + ".txt"):
            x = names.index(n)
            print info[x].comment,
    
    file = open(filename,'r')
    # print filename
     
    
    