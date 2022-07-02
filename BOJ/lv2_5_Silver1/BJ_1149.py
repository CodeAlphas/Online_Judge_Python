"""
 백준 1149번: RGB거리 풀이
 Author: CodeAlphas
 Date: 2022/06/15
 Problem Source: https://www.acmicpc.net/problem/1149
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input()) # 집의 수

dp = [[0, 0, 0] for _ in range(n)]
dp_r = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    dp[i][0], dp[i][1], dp[i][2] = map(int, input().split())

dp_r[0][0], dp_r[0][1], dp_r[0][2] = dp[0][0], dp[0][1], dp[0][2]
for i in range(1, n):
    dp_r[i][0] = dp[i][0] + min(dp_r[i-1][1], dp_r[i-1][2])
    dp_r[i][1] = dp[i][1] + min(dp_r[i-1][0], dp_r[i-1][2]) 
    dp_r[i][2] = dp[i][2] + min(dp_r[i-1][0], dp_r[i-1][1])

print(min(dp_r[n-1]))  
