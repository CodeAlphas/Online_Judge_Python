"""
 백준 2292번: 벌집 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/2292
 Version: Python 3.10.4
"""

n = int(input())
m = 1

while n > 3 * m * m - 3 * m + 1:
    m += 1

print(m)

