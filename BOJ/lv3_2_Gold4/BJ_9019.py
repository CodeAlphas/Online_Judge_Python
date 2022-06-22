"""
 백준 9019번: DSLR 풀이
 Author: CodeAlphas
 Date: 2022/06/11
 Problem Source: https://www.acmicpc.net/problem/9019
 Version: Python 3.10.4
"""

# PyPy3만 통과

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def check(a, b):
    global visited
    queue = deque([(a, "")])

    while queue:
        a, result = queue.popleft()

        if not visited[a]:
            visited[a] = True

            for i in range(4):
                if i == 0:
                    a_ = 2*a % 10000
                    if a_ == b: return result + 'D'
                    queue.append((a_, result + 'D'))
                elif i == 1:
                    if a != 0: a_ = a - 1
                    else: a_ = 9999
                    if a_ == b: return result + 'S'
                    queue.append((a_, result + 'S'))
                elif i == 2:
                    a_ = (a % 1000) * 10 + (a // 1000)
                    if a_ == b: return result + 'L'
                    queue.append((a_, result + 'L'))
                elif i == 3:
                    a_ = (a % 10) * 1000 + (a // 10)
                    if a_ == b: return result + 'R'                    
                    queue.append((a_, result + 'R'))

for test_case in range(t):
    visited = [False] * 10001
    a, b = map(int, input().split())
    print(check(a, b))
