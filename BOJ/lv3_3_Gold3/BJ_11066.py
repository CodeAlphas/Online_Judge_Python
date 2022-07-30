"""
 백준 11066번: 파일 합치기 풀이
 Author: CodeAlphas
 Date: 2022/07/10
 Problem Source: https://www.acmicpc.net/problem/11066
 Version: Python 3.10.4
"""

# PyPy3만 통과
import sys
input = sys.stdin.readline
INF = int(1e10)

t = int(input())

for test_case in range(t):
    k = int(input()) # 소설을 구성하는 장의 수

    chapters = list(map(int, input().split()))

    dp = [[0] * k for _ in range(k)]
    for y in range(1, k):
        for x in range(y-1, -1, -1):
            result = INF
            for idx in range(x, y):
                result = min(result, dp[x][idx] + dp[idx+1][y])
            dp[x][y] = result + sum(chapters[x:y+1])

    print(dp[0][k-1])