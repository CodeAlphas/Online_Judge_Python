"""
 백준 1904번: 01타일 풀이
 Author: CodeAlphas
 Date: 2022/07/23
 Problem Source: https://www.acmicpc.net/problem/1904
 Version: Python 3.10.4
"""

n = int(input())
dp = [0] * (n+1)

if n == 1:
    dp[1] = 1
elif n == 2:
    dp[1] = 1; dp[2] = 2
else:
    dp[1] = 1; dp[2] = 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])