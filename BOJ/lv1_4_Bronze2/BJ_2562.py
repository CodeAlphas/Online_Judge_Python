"""
 백준 2562번: 최댓값 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/2562
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
array = []

for i in range(9):
    array.append(int(input()))

a = max(array)
print(a)
print(array.index(a) + 1)