"""
 백준 24444번: 알고리즘 수업 - 너비 우선 탐색 1 풀이
 Author: CodeAlphas
 Date: 2022/08/22
 Problem Source: https://www.acmicpc.net/problem/24444
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

visited = [False] * (n+1) 
results = [0] * (n+1); order = 1

def bfs(r):
    global results, visited, order 

    visited[r] = True
    results[r] = order
    queue = deque([r])

    while queue:
        u = queue.popleft()
        for i in graph[u]:
            if visited[i] == False:
                order += 1
                results[i] = order
                queue.append(i)
                visited[i] = True

bfs(r)
for i in results[1:]:
    print(i)