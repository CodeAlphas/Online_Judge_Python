"""
 백준 11051번: 이항 계수 2 풀이
 Author: CodeAlphas
 Date: 2022/07/27
 Problem Source: https://www.acmicpc.net/problem/11051
 Version: Python 3.10.4
"""

n, k = map(int, input().split())

dp = [1] * (n + 1)
for i in range(1, n+1):
    dp[i] = (dp[i-1] * i) 

print((dp[n]//(dp[n-k]*dp[k])) % 10007)