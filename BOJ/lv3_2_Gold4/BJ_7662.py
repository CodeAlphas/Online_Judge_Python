"""
 백준 7662번: 이중 우선순위 큐 풀이
 Author: CodeAlphas
 Date: 2022/06/07
 Problem Source: https://www.acmicpc.net/problem/7662
 Version: Python 3.10.4
"""

import sys
import heapq
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수

for test_case in range(t):
    k = int(input()) # 각 테스트 케이스에 적용할 연산의 개수
    min_q = []; max_q = []; visited = [False] * k
    for i in range(k):
        op = input().split()
        if 'I' in op:
            heapq.heappush(min_q, (int(op[1]), i))
            heapq.heappush(max_q, (-int(op[1]), i))
            visited[i] = True
        else:
            if '-1' in op:
                while min_q and not visited[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visited[heapq.heappop(min_q)[1]] = False
            else:
                while max_q and not visited[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visited[heapq.heappop(max_q)[1]] = False
                
    while min_q and not visited[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)

    if min_q and max_q:
        print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
    else:
        print('EMPTY')
