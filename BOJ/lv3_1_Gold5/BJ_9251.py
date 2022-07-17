"""
 백준 9251번: LCS 풀이
 Author: CodeAlphas
 Date: 2022/06/26
 Problem Source: https://www.acmicpc.net/problem/9251
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

a = input().rstrip(); len_a = len(a) + 1
b = input().rstrip(); len_b = len(b) + 1

dp = [[0] * len_b for _ in range(len_a)]

for i in range(1, len_a):
    for j in range(1, len_b):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])