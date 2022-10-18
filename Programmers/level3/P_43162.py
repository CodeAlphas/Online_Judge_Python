"""
 프로그래머스: 네트워크 풀이
 Author: CodeAlphas
 Date: 2022/10/18
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/43162
 Version: Python 3.10.4
"""

visited = []
def dfs(graph, i):
    global visited
    visited[i] = True
    
    for node in graph[i]:
        if not visited[node]:
            dfs(graph, node)

def solution(n, computers):
    global visited
    answer = 0
    graph = [[] for _ in range(n+1)]
    for x in range(n):
        for y in range(n):
            if x != y and computers[x][y] == 1:
                graph[x+1].append(y+1)
    
    visited = [False] * (n+1)
    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i)
            answer += 1
    
    return answer