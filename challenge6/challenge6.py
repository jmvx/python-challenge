#!/usr/bin/env python

file = open('/Users/julia/Google Drive/Projects/python-challenge/challenge6/channel/90052.txt','r')
    
while True:
    contents = file.readlines()

    for line in contents:
        pieces = line.split(' ')
        print(pieces)
    
    filename = "/Users/julia/Google Drive/Projects/Python Challenge/challenge6/channel/" + pieces[len(pieces)-1] + ".txt"
    file = open(filename,'r')
    # print filename
 


