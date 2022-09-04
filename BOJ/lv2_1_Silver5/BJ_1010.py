"""
 백준 1010번: 다리 놓기 풀이
 Author: CodeAlphas
 Date: 2022/09/04
 Problem Source: https://www.acmicpc.net/problem/1010
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())
result = 0

while t:
    result = 0
    n, m = map(int, input().split())
    numerator = 1; denominator = 1
    for _ in range(n):
        numerator *= m
        m -= 1
    while n != 1:
        denominator *= n
        n -= 1
    print(numerator//denominator)
    t -= 1