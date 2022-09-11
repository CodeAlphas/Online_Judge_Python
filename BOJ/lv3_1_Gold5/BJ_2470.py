"""
 백준 2470번: 두 용액 풀이
 Author: CodeAlphas
 Date: 2022/09/11
 Problem Source: https://www.acmicpc.net/problem/2470
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
features = list(map(int, input().split()))
features.sort()

result = int(1e10)
left = 0; right = n-1

while left < right:
    sum = features[left] + features[right]
    abs_sum = abs(features[left] + features[right])
    
    if result > abs_sum:
        result = abs_sum
        ans = [features[left], features[right]]
    
    if sum > 0:
        right -= 1
    elif sum < 0:
        left += 1
    else:
        break

print(*ans)