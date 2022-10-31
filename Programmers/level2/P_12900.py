"""
 프로그래머스: 2 x n 타일링 풀이
 Author: CodeAlphas
 Date: 2022/10/31
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12900
 Version: Python 3.10.4
"""

def solution(n):
    dp = [0] * (n + 1)
    if n == 1:
        dp[1] = 1
    elif n >= 2:
        dp[1] = 1; dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
            
    return dp[n]