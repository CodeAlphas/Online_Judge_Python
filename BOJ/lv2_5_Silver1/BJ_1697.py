"""
 백준 1697번: 숨바꼭질 풀이
 Author: CodeAlphas
 Date: 2022/05/30
 Problem Source: https://www.acmicpc.net/problem/1697
 Version: Python 3.10.4
"""

from collections import deque
n, k = map(int, input().split())
visited = [0] * 100001

def move():
    queue = deque([n])

    while queue:
        n_ = queue.popleft()
        if n_ == k:
            return visited[n_]

        for nn in [n_-1, n_+1, 2*n_]:
            if 0 <= nn < 100001 and visited[nn] == 0:
                queue.append(nn)
                visited[nn] = visited[n_] + 1

print(move())