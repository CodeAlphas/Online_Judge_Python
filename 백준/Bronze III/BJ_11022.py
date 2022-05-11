"""
 백준 11022번: A+B - 8 풀이
 Author: CodeAlphas
 Date: 2022/04/14
 Problem Source: https://www.acmicpc.net/problem/11022
 Version: Python 3.10.4
"""

import sys

t = int(sys.stdin.readline())

for i in range(1, t+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(i, a, b, a + b))
