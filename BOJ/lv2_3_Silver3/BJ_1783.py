"""
 백준 1783번: 병든 나이트 풀이
 Author: CodeAlphas
 Date: 2022/08/27
 Problem Source: https://www.acmicpc.net/problem/1783
 Version: Python 3.10.4
"""

n, m = map(int, input().split())

def check(n, m):
    if n == 1:
        return 1
    elif n == 2:
        return min(4, (m - 1) // 2 + 1)
    else:
        if m < 7:
            return min(4, m)
        else:
            return m - 2

print(check(n, m))