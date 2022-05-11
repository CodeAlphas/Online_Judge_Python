"""
 백준 2579번: 계단 오르기 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2579
 Version: Python 3.10.4
"""

n = int(input())
stairs = []
dp = [0 for _ in range(300)]

for i in range(n):
    stairs.append(int(input()))

if n == 1:
    dp[0] = stairs[0]
elif n == 2:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]    
elif n >= 3:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n-1])