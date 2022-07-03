"""
 백준 11286번: 절댓값 힙 풀이
 Author: CodeAlphas
 Date: 2022/06/16
 Problem Source: https://www.acmicpc.net/problem/11286
 Version: Python 3.10.4
"""

import sys
import heapq
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if array:
            x, n = heapq.heappop(array)
            print(x * n)
        else:
            print(0)
    else:
        if x >= 0:
            n = 1
        else:
            n = -1; x = -x
        heapq.heappush(array, (x, n))