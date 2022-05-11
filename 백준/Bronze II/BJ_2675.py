"""
 백준 2675번: 문자열 반복 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2675
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    r, s = input().split() 
    n = 0
    s_len = len(s)

    while n < s_len:
        for j in range(int(r)):
            print(s[n], end = '')
        n += 1
    print()
