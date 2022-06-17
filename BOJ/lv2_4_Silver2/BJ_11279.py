"""
 백준 11279번: 최대 힙 풀이
 Author: CodeAlphas
 Date: 2022/06/09
 Problem Source: https://www.acmicpc.net/problem/11279
 Version: Python 3.10.4
"""

import sys
import heapq
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, -x)
