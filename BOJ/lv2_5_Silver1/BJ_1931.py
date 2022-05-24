"""
 백준 1931번: 회의실 배정 풀이
 Author: CodeAlphas
 Date: 2022/05/21
 Problem Source: https://www.acmicpc.net/problem/1931
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())

i = []
for _ in range(n):
    i.append(tuple(map(int, input().split())))
i.sort(key=lambda x: (x[1], x[0]))
result = 1
temp = i[0]

for m in range(1, n):
    if i[m][0] >= temp[1]:
        temp = i[m]
        result += 1

print(result)



