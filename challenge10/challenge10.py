#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/return/bull.html

# a = [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

def bull(n):   
    x = '_' + str(n)
    y = str(n)
    tups = zip(x, y)
    count = 0
    storage = []
    
    for prev, this in tups:
        if prev == '_' or prev == this:
            count += 1
        else:
            storage.append(count), storage.append(prev)
            count = 1
    
    storage.append(count), storage.append(this)
    answer = int(''.join(map(str, storage)))
    return answer
    
    
    # ORIGINAL VERSION ######################
    # num, same, answer = str(n), [], []
    # for i in xrange(len(num)):
    #     if i == 0 or (num[i] == num[i-1]):
    #         same.append(num[i])
    #     else:
    #         if len(same) > 0:
    #             answer.append(len(same))
    #             answer.append(same[0])
    #         same = []
    #         same.append(num[i])
    # if len(same) > 0:
    #     answer.append(len(same))
    #     answer.append(same[0])
    #
    # s = int(''.join(map(str, answer)))
    # return s
    ########################################


# Pass in values
next = bull(1) # 1st
for i in xrange(0,29): # 29 more
    next = bull(next)
print len(str(next))
