#!/bin/python

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    length = len(arr)
    new = []
    for i in range(length):
        el = [arr[i], i]
        new.append(el)
        
    new_arr = sorted(new)
    if length < 2:
        return 0
        
    left = 0
    right = length - 1

    while True:
        
        if new_arr[left][0] + new_arr[right][0] > m:
            right -= 1
        elif new_arr[left][0] + new_arr[right][0] < m:
            left += 1

        if new_arr[left][0] + new_arr[right][0] == m or left == right:
            break
    res = []
    if new_arr[left][0] + new_arr[right][0] == m:
        res.append(new_arr[left][1] + 1)
        res.append(new_arr[right][1] + 1)
        
    new = sorted(res)
    print  new
    return new
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        m = int(raw_input())

        n = int(raw_input())

        arr = map(int, raw_input().rstrip().split())

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
