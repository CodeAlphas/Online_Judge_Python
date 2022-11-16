"""
 프로그래머스: 게임 맵 최단거리 풀이
 Author: CodeAlphas
 Date: 2022/11/16
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/1844
 Version: Python 3.10.4
"""

from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def check(maps, n, m):
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, c = queue.popleft()
        if x == n - 1 and y == m - 1:
            return c
        else:
            for i in range(4):
                nx = x + dirs[i][0]; ny = y + dirs[i][1]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny, c + 1))
    return -1
                
def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    answer = check(maps, n, m)
    return answer