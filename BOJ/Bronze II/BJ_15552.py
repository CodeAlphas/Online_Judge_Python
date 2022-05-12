"""
 백준 15552번: 빠른 A+B 풀이
 Author: CodeAlphas
 Date: 2022/04/16
 Problem Source: https://www.acmicpc.net/problem/15552
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())

while t > 0:
    a, b = map(int, input().split())
    print(a + b)
    t -= 1