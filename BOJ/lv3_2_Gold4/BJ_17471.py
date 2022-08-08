"""
 백준 17471번: 게리맨더링 풀이
 Author: CodeAlphas
 Date: 2022/07/19
 Problem Source: https://www.acmicpc.net/problem/17471
 Version: Python 3.10.4
"""

import sys
import copy
from collections import deque
input = sys.stdin.readline
INF = int(1e10)

n = int(input()); result = INF
list_n = [i for i in range(1, n+1)]
numbers = [0] + list(map(int, input().split()))
sum_numbers = sum(numbers)

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    links = list(map(int, input().split()))[1:]
    for link in links:
        graph[i].append(link)

def islinked(list_a):
    s = list_a[0]
    queue = deque([(s, 0)])
    len_s = len(list_a)
    visited = [0] * len_s

    while queue:
        ns, idx = queue.popleft()
        visited[idx] = 1
        for i in range(len_s):
            if visited[i] == 0 and (list_a[i] in graph[ns]):
                queue.append((list_a[i], i))

    if sum(visited) == len_s:
        return True
    else:
        return False
    
def check(list_a, list_b):
    global numbers, sum_numbers, result

    if islinked(list_a) and islinked(list_b):
        temp = 0
        for i in list_a:
            temp += numbers[i]
        temp_ = abs(2 * temp - sum_numbers)
        result = min(result, temp_)

def divide(depth, num, list_a, visited):
    global list_n

    if depth == num:
        check(list_a, list(set(list_n) - set(list_a)))

    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            divide(depth+1, num, list_a + [i], copy.deepcopy(visited))

for i in range(1, n//2+1):
    visited = [0] * (n+1)
    divide(0, i, [], visited)

if result == INF:
    print(-1)
else:
    print(result)