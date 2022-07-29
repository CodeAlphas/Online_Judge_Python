"""
 백준 12865번: 평범한 배낭 풀이
 Author: CodeAlphas
 Date: 2022/07/09
 Problem Source: https://www.acmicpc.net/problem/12865
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]

for x in range(1, n+1):
    w, v = map(int, input().split())
    for y in range(1, k+1):
        if y >= w:
            dp[x][y] = max(dp[x-1][y], dp[x-1][y-w] + v)
        else:
            dp[x][y] = dp[x-1][y] 

print(dp[n][k])