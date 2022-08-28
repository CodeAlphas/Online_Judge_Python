"""
 백준 2477번: 참외밭 풀이
 Author: CodeAlphas
 Date: 2022/08/28
 Problem Source: https://www.acmicpc.net/problem/2477
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

k = int(input())

shape = []
for _ in range(6):
    shape.append(tuple(map(int, input().split())))

big_rect = 0
for i in range(6):
    temp_rect = shape[i][1] * shape[(i+1) % 6][1]
    if temp_rect > big_rect:
        idx = i
        big_rect = temp_rect

small_rect = abs(shape[(idx-1) % 6][1] - shape[(idx+1) % 6][1]) * \
             abs(shape[idx % 6][1] - shape[(idx+2) % 6][1])
print(k * (big_rect - small_rect))