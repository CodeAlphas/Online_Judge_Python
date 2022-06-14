"""
 백준 11726번: 2×n 타일링 풀이
 Author: CodeAlphas
 Date: 2022/06/05
 Problem Source: https://www.acmicpc.net/problem/11726
 Version: Python 3.10.4
"""

n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n] % 10007)
