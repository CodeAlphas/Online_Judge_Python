"""
 백준 10773번: 제로 풀이
 Author: CodeAlphas
 Date: 2022/05/15
 Problem Source: https://www.acmicpc.net/problem/10773
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

k = int(input())
result = []

for _ in range(k):
    n = int(input())
    if n != 0:
        result.append(n)
    else:
        result.pop()

print(sum(result))

    