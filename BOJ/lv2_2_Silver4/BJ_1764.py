"""
 백준 1764번: 듣보잡 풀이
 Author: CodeAlphas
 Date: 2022/05/26
 Problem Source: https://www.acmicpc.net/problem/1764
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

h_name = {}
names = []; count = 0

for _ in range(n):
    h_name[input().strip()] = 1

for _ in range(m):
    name = input().strip() 
    if name in h_name:
        count += 1
        names.append(name)

print(count); names.sort()
for name in names:
    print(name)