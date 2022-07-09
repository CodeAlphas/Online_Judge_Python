"""
 백준 1932번: 정수 삼각형 풀이
 Author: CodeAlphas
 Date: 2022/06/19
 Problem Source: https://www.acmicpc.net/problem/1932
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[0] * i for i in range(0, n+1)]
dp[1] = triangle[0]

for i in range(2, n+1):
    for j in range(i):
        if j == 0:
            dp[i][j] = dp[i-1][j] + triangle[i-1][j]
        elif j == i-1:
            dp[i][j] = dp[i-1][j-1] + triangle[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i-1][j]

print(max(dp[n]))



