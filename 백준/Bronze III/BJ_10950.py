"""
 백준 10950번: A+B - 3 풀이
 Author: CodeAlphas
 Date: 2022/04/28
 Problem Source: https://www.acmicpc.net/problem/10950
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())

while t > 0:
    a, b = map(int, input().split())
    print(a + b)
    t -= 1
