#!/bin/python

import sys

def solve(a):
    left = 0
    right = len(a)
    left_sum = a[0]
    right_sum = a[-1]
    result = 'YES'
    
    while left + 1 < right:
        if left_sum <= right_sum:
            left += 1
            left_sum += a[left]
        else:
            right -= 1
            right_sum += a[right]
        
        if right_sum == left_sum and right == left + 2:
            result = 'NO'
    
    return result
    
T = int(raw_input().strip())
for a0 in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = solve(a)
    print(result)