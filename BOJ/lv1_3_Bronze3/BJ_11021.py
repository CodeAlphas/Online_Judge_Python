"""
 백준 11021번: A+B - 7 풀이
 Author: CodeAlphas
 Date: 2022/04/14
 Problem Source: https://www.acmicpc.net/problem/11021
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())

    print("Case #%d: %d" %(i, a+b))