"""
 백준 2252번: 줄 세우기 풀이
 Author: CodeAlphas
 Date: 2022/10/01
 Problem Source: https://www.acmicpc.net/problem/2252
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

def topology_sort():
    global result, in_degree

    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0: queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0: queue.append(i)

topology_sort()
print(*result)