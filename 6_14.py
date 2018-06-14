#!/bin/python

import os
import sys

# Complete the substringDiff function below.
def substringDiff(k, s1, s2):
    
    left = 0
    right = 0
    max_seq = 0
    cur_sum = 0
    length = len(s1)
    
    while True:
        cur_sum += diff(s1, s2, right)
        print cur_sum, right, diff(s1, s2, right)
        while cur_sum > k:
            print '  ', cur_sum, max_seq, right, left
            max_seq=max(max_seq, right-left - 1)
            print max_seq
            cur_sum -= diff(s1, s2, left)
            left += 1
        
        right += 1
        if right >= length:
            break
            
    return max_seq+1
    
def diff(s1, s2, index):
    if ord(s1[index]) - ord(s2[index]) != 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        kS1S2 = raw_input().split()

        k = int(kS1S2[0])

        s1 = kS1S2[1]

        s2 = kS1S2[2]

        result = substringDiff(k, s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
