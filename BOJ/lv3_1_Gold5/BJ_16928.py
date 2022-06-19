"""
 백준 16928번: 뱀과 사다리 게임 풀이
 Author: CodeAlphas
 Date: 2022/06/10
 Problem Source: https://www.acmicpc.net/problem/16928
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split()) # 사다리의 수, 뱀의 수
ladders_snakes = [-1] * 101; result = int(1e10)
visited = [False] * 101

for _ in range(n+m):
    a, b = map(int, input().split())
    ladders_snakes[a] = b

def bfs():
    global result

    queue = deque([(1, 0)])
    visited[1] = True

    while queue:
        x, c = queue.popleft()

        if x == 100:
            result = min(result, c)
            continue

        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            elif not visited[nx]:
                visited[nx] = True
                if ladders_snakes[nx] != -1:
                    nx = ladders_snakes[nx]
            else:
                continue

            queue.append((nx, c+1))

bfs()
print(result)

