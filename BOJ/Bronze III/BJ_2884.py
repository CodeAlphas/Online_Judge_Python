"""
 백준 2884번: 알람 시계 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2884
 Version: Python 3.10.4
"""

h, m = map(int, input().split())

if m >= 45:
    m -= 45
else:
    if h == 0:
        h = 23
    else:
        h -= 1
    m = 60 + m - 45

print(h, m)