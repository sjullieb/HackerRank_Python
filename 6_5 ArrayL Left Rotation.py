#!/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    length = len(a)
    
    index_from = 0
    item_from = a[0]
    index_to = 0
    i = 0
    count = 0
    while True:
        count += 1
        index_to = (length + index_from - d) % length
        print index_from, index_to, item_from
        tmp = a[index_to]
        a[index_to] = item_from
        index_from = index_to
        item_from = tmp
        
        if index_from == i and count <> length:
            i += 1
            index_from = i
            item_from = a[i]
        elif count == length:
            break
    print a
    return a

def rotLeftAdditionalArr(a, d):
    length = len(a)
    res = []
    for i in range(length):
        res.append(a[(i + d)%length])
    print res
    return res
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
