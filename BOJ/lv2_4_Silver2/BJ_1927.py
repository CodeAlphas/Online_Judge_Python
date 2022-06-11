"""
 백준 1927번: 최소 힙 풀이
 Author: CodeAlphas
 Date: 2022/06/02
 Problem Source: https://www.acmicpc.net/problem/1927
 Version: Python 3.10.4
"""

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    number = int(input())
    if number == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, number)
