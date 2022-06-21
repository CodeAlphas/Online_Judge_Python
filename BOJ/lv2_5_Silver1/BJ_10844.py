"""
 백준 10844번: 쉬운 계단 수 풀이
 Author: CodeAlphas
 Date: 2022/06/10
 Problem Source: https://www.acmicpc.net/problem/10844
 Version: Python 3.10.4
"""

n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0] + [1] * 9

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]

print(sum(dp[n]) % 1000000000)