"""
 백준 5430번: AC 풀이
 Author: CodeAlphas
 Date: 2022/05/26
 Problem Source: https://www.acmicpc.net/problem/5430
 Version: Python 3.10.4
"""

import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) # 테스트 케이스 개수

for test_case in range(t):

    p = input().rstrip() # 수행할 함수
    n = int(input()) # 배열에 들어있는 수의 개수
    x = input().rstrip() # 배열에 들어있는 정수
    x = x[1:-1]
    if x == "":
        queue = deque()
    else:
        queue = deque(x.split(","))

    len_p = len(p)
    ch = True; ch1 = False
    for i in range(len_p):
        if p[i] == "R":
            ch = not ch
        else:
            if queue:
                if ch:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print("error")
                ch1 = True
                break

    if ch1: continue
    else:
        if not ch:
            queue.reverse()
        if queue:
            print("[" + ",".join(list(queue)) + "]")
        else:
            print("[]")           


