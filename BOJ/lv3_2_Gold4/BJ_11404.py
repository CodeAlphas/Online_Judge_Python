"""
 백준 11404번: 플로이드 풀이
 Author: CodeAlphas
 Date: 2022/07/07
 Problem Source: https://www.acmicpc.net/problem/11404
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
INF = int(1e10)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y: graph[x][y] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] != INF:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c
        
for i in range(1, n+1):
    for x in range(1, n+1):
        for y in range(1, n+1):
            graph[x][y] = min(graph[x][y], graph[x][i]+graph[i][y])

for x in range(1, n+1):
  for y in range(1, n+1):
    if graph[x][y] == INF:
      print("0", end = " ")
    else:
      print(graph[x][y], end = " ")
  print()