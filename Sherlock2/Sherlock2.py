#!/bin/python

import sys

def solve(a):
    left = -1
    right = len(a)
    left_sum = 0#a[0]
    right_sum = 0#a[-1]
    result = 'YES'
    print a
    while left + 1 < right:
        if left_sum <= right_sum:
            left += 1
            left_sum += a[left]
        else:
            right -= 1
            right_sum += a[right]
            
        print left, left_sum, 'left-right', right, right_sum
        if right_sum == left_sum and right == left + 2:
            result = 'YES'
        else:
            result = 'NO'
    
    return result
    
T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)
