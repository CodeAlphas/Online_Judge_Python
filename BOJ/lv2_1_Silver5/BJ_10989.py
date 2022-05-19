"""
 백준 10989번: 수 정렬하기 3 풀이
 Author: CodeAlphas
 Date: 2022/05/17
 Problem Source: https://www.acmicpc.net/problem/10989
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())

count = [0] * (10000 + 1)

for i in range(n):
    count[int(input())] += 1

len_count = len(count)
for i in range(len_count):
    for j in range(count[i]):
        print(i)





