"""
 백준 1389번: 케빈 베이컨의 6단계 법칙 풀이
 Author: CodeAlphas
 Date: 2022/05/24
 Problem Source: https://www.acmicpc.net/problem/1389
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 유저의 수, 친구 관계의 수
INF = int(10e9)
result = INF
graph = [[INF]*(n+1) for _ in range(n+1)]    

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
        
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1; graph[b][a] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for l in range(1, n+1):
    temp = sum(graph[l][1:])
    if result > temp:
        result = temp
        ans = l

print(ans)