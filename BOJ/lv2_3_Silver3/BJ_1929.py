"""
 백준 1929번: 소수 구하기 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/1929
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

m, n = map(int, input().split())
array = [True for _ in range(n+1)]
array[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(m, n+1):
    if array[i] == True:
        print(i)