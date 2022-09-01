"""
 백준 25305번: 커트라인 풀이
 Author: CodeAlphas
 Date: 2022/09/01
 Problem Source: https://www.acmicpc.net/problem/25305
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)

print(scores[k-1])