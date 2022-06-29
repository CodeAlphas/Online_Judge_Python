"""
 백준 1260번: DFS와 BFS 풀이
 Author: CodeAlphas
 Date: 2022/06/13
 Problem Source: https://www.acmicpc.net/problem/1260
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graphs = [[] for _ in range(n+1)]

temp = []
for _ in range(m):
    a, b = map(int, input().split())
    temp.append((a, b))

temp = list(set(temp))
for a, b in temp:
    graphs[a].append(b)
    graphs[b].append(a)

for graph in graphs:
    graph.sort()

visited = [False] * (n+1)
def dfs(v):
    visited[v] = True
    print(v, end = ' ')

    for i in graphs[v]:
        if not visited[i]:
            dfs(i)
dfs(v)
print()

visited = [False] * (n+1)
def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in graphs[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(v)
