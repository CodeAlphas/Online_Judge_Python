"""
 백준 10951번: A+B - 4 풀이
 Author: CodeAlphas
 Date: 2022/04/28
 Problem Source: https://www.acmicpc.net/problem/10951
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
