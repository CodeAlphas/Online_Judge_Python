"""
 백준 11724번: 연결 요소의 개수 풀이
 Author: CodeAlphas
 Date: 2022/05/31
 Problem Source: https://www.acmicpc.net/problem/11724
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n)]
visited = {}
count = 0

for i in range(n):
    visited[i] = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1); graph[b-1].append(a-1)

def check(index):
    global count 
    queue = deque([index])
    visited[index] = True
    count += 1
    while queue:
        a = queue.popleft()
        
        for a_ in graph[a]:
            if not visited[a_]:
                visited[a_] = True
                queue.append(a_)
        
for i in range(n):
    if not visited[i]:
        check(i)

print(count)

