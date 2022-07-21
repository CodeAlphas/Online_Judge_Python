"""
 백준 1238번: 파티 풀이
 Author: CodeAlphas
 Date: 2022/06/30
 Problem Source: https://www.acmicpc.net/problem/1238
 Version: Python 3.10.4
"""

import sys
import heapq
input = sys.stdin.readline
INF = int(1e10)

n, m, x = map(int, input().split())
maps = [[] for _ in range(n+1)]; distance = [INF] * (n+1)
maps_ = [[] for _ in range(n+1)]; distance_ = [INF] * (n+1)

for _ in range(m):
    start, end, time = map(int, input().split())
    maps[start].append((end, time))
    maps_[end].append((start, time))

def dijkstra(start, maps, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in maps[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x, maps, distance)
dijkstra(x, maps_, distance_)
dis = 0
for i in range(1, n+1):
    distance[i] += distance_[i]
    if dis < distance[i]:
        dis = distance[i]

print(dis)