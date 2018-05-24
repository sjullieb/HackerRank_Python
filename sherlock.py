#!/bin/python

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    result = 'NO'
    dict = {}
    for ch in range(ord('a'), ord('z')):
        dict[chr(ch)] = 0

    for ch in s:
        dict[ch] += 1

    print()    
    
    print ('1 ' + str(dict))
    count = {}
    for ch in dict:
        print ch
        if dict[ch] > 0:
            if count.has_key(dict[ch]) == True:
                count[dict[ch]] += 1
                print 'updating ' + ch
            else:
                count[dict[ch]] = 1
                print 'adding ' + ch
            print count


    if len(count) > 2 or len(count) == 0:
        result = 'NO'
    elif len(count) == 1:
        result = 'YES'
    else:
        items = sorted(count.items())
        print items
        first = items[0][1]
        f_key = items[0][0]
        second = items[1][1]
        s_key = items[1][0]
        if (abs(int(f_key) - int(s_key))==1 and (first == 1 or second == 1)) or (first == 1 and f_key == 1) or (second == 1 and s_key == 1):
            result = 'YES'
        else:
            result = 'NO'
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
