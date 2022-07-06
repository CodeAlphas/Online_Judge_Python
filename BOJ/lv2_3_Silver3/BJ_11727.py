"""
 백준 11727번: 2×n 타일링 2 풀이
 Author: CodeAlphas
 Date: 2022/06/17
 Problem Source: https://www.acmicpc.net/problem/11727
 Version: Python 3.10.4
"""

n = int(input())
dp = [0] * (n+1)

if n == 1:
    dp[1] = 1
else:
    dp[1] = 1; dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)