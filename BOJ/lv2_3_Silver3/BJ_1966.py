"""
 백준 1966번: 프린터 큐 풀이
 Author: CodeAlphas
 Date: 2022/05/20
 Problem Source: https://www.acmicpc.net/problem/1966
 Version: Python 3.10.4
"""

from collections import deque
import sys
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 수

for test_case in range(t):
    queue = deque() # 각 문서의 중요도
    n, m = map(int, input().split()) # 문서의 개수, 몇 번째로 인쇄 되었는지 궁금한 문서
    temp = list(map(int, input().split()))
    len_temp = len(temp)
    for i in range(len_temp):
        if i == m:
            queue.append((temp[i], 1))
        else:
            queue.append((temp[i], 0))            
    result = 1 # 인쇄 순서

    while queue:
        i = queue[0][0]; c = queue[0][1]
        if c == 1:
            check = True
            for c_in in queue:
                if c_in[0] > i:
                    queue.popleft()
                    queue.append((i, 1))
                    check = False
                    break

            if check:
                print(result)
                queue = []
                break

        else:
            check = True
            for c_in in queue:
                if c_in[0] > i:
                    queue.popleft()
                    queue.append((i, 0))
                    check = False
                    break

            if check:
                queue.popleft()
                result += 1