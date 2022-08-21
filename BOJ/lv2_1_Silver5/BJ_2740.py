"""
 백준 2740번: 행렬 곱셈 풀이
 Author: CodeAlphas
 Date: 2022/08/21
 Problem Source: https://www.acmicpc.net/problem/2740
 Version: Python 3.10.4
"""

import sys
import copy
input = sys.stdin.readline

a = []; b = []
a_n, a_m = map(int, input().split())
for _ in range(a_n):
    a.append(list(map(int, input().split())))

b_m, b_k = map(int, input().split())
for _ in range(b_m):
    b.append(list(map(int, input().split())))

result = []
for i in range(a_n):
    t_array = []
    for j in range(b_k):
        temp = 0
        for k in range(a_m):
            temp += a[i][k] * b[k][j]
        t_array.append(temp)
    result.append(copy.deepcopy(t_array))

for i in range(a_n):
    print(*result[i])