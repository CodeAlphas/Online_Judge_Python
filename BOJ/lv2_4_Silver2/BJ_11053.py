"""
 백준 11053번: 가장 긴 증가하는 부분 수열 풀이
 Author: CodeAlphas
 Date: 2022/07/22
 Problem Source: https://www.acmicpc.net/problem/11053
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
dp = [1] * n; result = 0

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    result = max(result, dp[i])

print(result)