"""
 백준 10828번: 스택 풀이
 Author: CodeAlphas
 Date: 2022/05/03
 Problem Source: https://www.acmicpc.net/problem/10828
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input()) # 명령의 수
stack = []

for _ in range(1, n+1):
    order = input().split()
    len_order = len(order)

    if len_order == 1:
        if order[0] == "pop":
            if len(stack) >= 1:
                print(stack.pop())
            else:
                print(-1)
        elif order[0] == "size":
            print(len(stack))
        elif order[0] == "empty":
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) >= 1:
                print(stack[-1])
            else:
                print(-1)
    else:
        a = int(order[1])
        stack.append(a)
        
