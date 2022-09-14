"""
 백준 1049번: 기타줄 풀이
 Author: CodeAlphas
 Date: 2022/09/14
 Problem Source: https://www.acmicpc.net/problem/1049
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

p_cost = int(1e10); o_cost = int(1e10)
for _ in range(m):
    a, b = map(int, input().split())
    if p_cost > a:
        p_cost = a
    if o_cost > b:
        o_cost = b

if n > 6:
    result = min((n // 6) * p_cost + (n % 6) * o_cost, (n // 6 + 1) * p_cost, n * o_cost)
else:
    result = min(p_cost, n * o_cost)

print(result)