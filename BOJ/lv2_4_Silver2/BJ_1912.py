"""
 백준 1912번: 연속합 풀이
 Author: CodeAlphas
 Date: 2022/07/21
 Problem Source: https://www.acmicpc.net/problem/1912
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [0] * (n+1)
result = array[0]

for i in range(1, n+1):
    dp[i] = max(array[i-1], dp[i-1] + array[i-1])
    result = max(result, dp[i])

print(result)