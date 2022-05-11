"""
 백준 10952번: A+B - 5 풀이
 Author: CodeAlphas
 Date: 2022/04/28
 Problem Source: https://www.acmicpc.net/problem/10952
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break

    print(a+b)

