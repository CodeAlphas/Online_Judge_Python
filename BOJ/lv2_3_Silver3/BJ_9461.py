"""
 백준 9461번: 파도반 수열 풀이
 Author: CodeAlphas
 Date: 2022/06/11
 Problem Source: https://www.acmicpc.net/problem/9461
 Version: Python 3.10.4
"""

t = int(input())
dp = [0, 1, 1] + [0] * 98

for test_case in range(t):
    n = int(input())
    for i in range(3, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[n])
