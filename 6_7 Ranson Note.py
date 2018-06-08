#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict = dict()
    for word in magazine:
        if word in mag_dict:
            mag_dict[word] += 1
        else:
            mag_dict[word] = 1
    
    for word in note:
        number = mag_dict.get(word, 0)
        if number == 0:
            print 'No'
            return
        else:
            mag_dict[word] -= 1
    
    print 'Yes'
        
if __name__ == '__main__':
    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = raw_input().rstrip().split()

    note = raw_input().rstrip().split()

    checkMagazine(magazine, note)
