"""
 백준 1753번: 최단경로 풀이
 Author: CodeAlphas
 Date: 2022/07/02
 Problem Source: https://www.acmicpc.net/problem/1753
 Version: Python 3.10.4
"""

import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
INF = int(10e9)

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for _ in range(e):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


