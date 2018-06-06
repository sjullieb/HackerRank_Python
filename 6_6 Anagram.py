#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    a = raw_input()

    b = raw_input()
    
dic = []
for i in range(26):
        dic.append(0)
        
for ch in a:
    dic[ord(ch) - ord('a')] += 1

for ch in b:
    dic[ord(ch) - ord('a')] -= 1
#print dic
counter = 0
for num in dic:
    if num != 0: counter += abs(num)

print counter
