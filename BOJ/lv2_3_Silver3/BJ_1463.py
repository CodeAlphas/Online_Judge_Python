"""
 백준 1463번: 1로 만들기 풀이
 Author: CodeAlphas
 Date: 2022/05/28
 Problem Source: https://www.acmicpc.net/problem/1463
 Version: Python 3.10.4
"""

n = int(input())
d = [0] * (n + 1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])