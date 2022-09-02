"""
 백준 2468번: 안전 영역 풀이
 Author: CodeAlphas
 Date: 2022/09/02
 Problem Source: https://www.acmicpc.net/problem/2468
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graphs = []
for _ in range(n):
    graphs.append(list(map(int, input().split())))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def check(visited, depth):
    count = 0

    for x in range(n):
        for y in range(n):
            if graphs[x][y] <= depth:
                visited[x][y] = True

    for x in range(n):
        for y in range(n):
            if visited[x][y] == False:
                count += 1
                queue = deque([(x, y)])
                visited[x][y] = True
                while queue:
                    x_, y_ = queue.popleft()    
                    for i in range(4):
                        nx = x_ + move[i][0]; ny = y_ + move[i][1]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                            visited[nx][ny] = True
                            queue.append((nx, ny)) 
                    
    return count

result = 0 # 안전한 영역의 최대 개수
for depth in range(0, 101):
    visited = [[False] * n for _ in range(n)]
    result = max(result, check(visited, depth))

print(result)