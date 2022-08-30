"""
 백준 1026번: 보물 풀이
 Author: CodeAlphas
 Date: 2022/08/30
 Problem Source: https://www.acmicpc.net/problem/1026
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = 0

for _ in range(n):
    min_a = min(a)
    max_b = max(b)
    result += min_a * max_b
    a.pop(a.index(min_a))
    b.pop(b.index(max_b))

print(result)