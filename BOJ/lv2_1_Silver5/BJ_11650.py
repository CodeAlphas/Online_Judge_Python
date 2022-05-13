"""
 백준 11650번: 좌표 정렬하기 풀이
 Author: CodeAlphas
 Date: 2022/05/12
 Problem Source: https://www.acmicpc.net/problem/11650
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
xy_list = []

for _ in range(n):
    x, y = map(int, input().split())
    xy_list.append((x, y))

xy_list.sort()

for x, y in xy_list:
    print(x, y)
