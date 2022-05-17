"""
 백준 11651번: 좌표 정렬하기 2 풀이
 Author: CodeAlphas
 Date: 2022/05/16
 Problem Source: https://www.acmicpc.net/problem/11651
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
xy = []

for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

xy.sort(key = lambda x : (x[1], x[0]))

for result in xy:
    print(result[0], result[1])

