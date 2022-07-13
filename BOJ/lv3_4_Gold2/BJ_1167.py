"""
 백준 1167번: 트리의 지름 풀이
 Author: CodeAlphas
 Date: 2022/06/23
 Problem Source: https://www.acmicpc.net/problem/1167
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
n = int(input())

tree = [[] for _ in range(n+1)]; search_node = []
for _ in range(n):
    i, *temp = list(map(int, input().split()))[:-1]
    temp_len = len(temp)
    for j in range(0, temp_len, 2):
        tree[i].append((temp[j], temp[j+1]))

result = 0; node = 0
def search(count, x, visited):
    global result, node
    result = max(count, result)
    visited[x] = True
    for i, c in tree[x]:
        if not visited[i]:
            if result < count + c:
                node = i
            search(count+c, i, visited)

visited = [False] * (n+1)
search(0, 1, visited)
visited = [False] * (n+1)
search(0, node, visited)
    
print(result)