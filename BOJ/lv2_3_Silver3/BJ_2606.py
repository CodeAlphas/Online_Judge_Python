"""
 백준 2606번: 바이러스 풀이
 Author: CodeAlphas
 Date: 2022/06/08
 Problem Source: https://www.acmicpc.net/problem/2606
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def check(node):
    global result
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            result += 1
            check(n)

check(1)
print(result)
