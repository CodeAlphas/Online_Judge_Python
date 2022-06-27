"""
 백준 6064번: 카잉 달력 풀이
 Author: CodeAlphas
 Date: 2022/06/12
 Problem Source: https://www.acmicpc.net/problem/6064
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())

def gcd(x, y):
    if y == 0:
        return x

    return gcd(y, x % y)

for test_case in range(t):
    m, n, x, y = map(int, input().split())
    a = x; count = x; end = m*n // gcd(m, n)
    if x % n == 0: b = n 
    else: b = x % n
    
    while count <= end:
        if b == y:
            print(count); break
        else:
            count += m
            if count % n == 0: b = n
            else: b = count % n
    else:
        print(-1)
