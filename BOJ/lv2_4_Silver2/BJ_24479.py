"""
 백준 24479번: 알고리즘 수업 - 깊이 우선 탐색 1 풀이
 Author: CodeAlphas
 Date: 2022/08/20
 Problem Source: https://www.acmicpc.net/problem/24479
 Version: Python 3.10.4
"""

import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

n, m, r = map(int, input().split())
graphs = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = [0] * (n+1); order = 1

for _ in range(m):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

for i in graphs:
    i.sort()

def dfs(r, visited):
    global result, order
    visited[r] = True
    result[r] = order

    for i in graphs[r]:
        if visited[i] == False:
            order += 1
            dfs(i, visited)
    return

dfs(r, visited)
for i in result[1:]:
    print(i)