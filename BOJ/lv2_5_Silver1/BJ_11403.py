"""
 백준 11403번: 경로 찾기 풀이
 Author: CodeAlphas
 Date: 2022/06/15
 Problem Source: https://www.acmicpc.net/problem/11403
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for a in range(n):
        for b in range(n):
            if graph[a][i] != 0 and graph[i][b] != 0:
                graph[a][b] = 1

for i in range(n):
    print(*graph[i])