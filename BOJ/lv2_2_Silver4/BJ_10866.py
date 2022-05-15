"""
 백준 10866번: 덱 풀이
 Author: CodeAlphas
 Date: 2022/05/13
 Problem Source: https://www.acmicpc.net/problem/10866
 Version: Python 3.10.4
"""

# 1
# import sys
# input = sys.stdin.readline

# n = int(input())
# deque = []

# for _ in range(n):
#     order = list(input().split())
#     len_order = len(order)

#     if len_order == 1:
#         if order[0] == "pop_front":
#             if deque:
#                 print(deque.pop(0))
#             else:
#                 print(-1)
#         elif order[0] == "pop_back":
#             if deque:
#                 print(deque.pop(-1))
#             else:
#                 print(-1)
#         elif order[0] == "size":
#             print(len(deque))
#         elif order[0] == "empty":
#             if deque:
#                 print(0)
#             else:
#                 print(1)
#         elif order[0] == "front":
#             if deque:
#                 print(deque[0])
#             else:
#                 print(-1)
#         else:
#             if deque:
#                 print(deque[-1])
#             else:
#                 print(-1)
#     else:
#         ord, value = order[0], order[1]
#         if ord == "push_front":
#             deque.insert(0, value)
#         else:
#             deque.append(value)

# 2
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    order = input().split()
    if "push_front" in order:
        d.appendleft(order[1])
    elif "push_back" in order:
        d.append(order[1])
    elif "pop_front" in order:
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif "pop_back" in order:
        if d:
            print(d.pop())
        else:
            print(-1)
    elif "size" in order:
        print(len(d))
    elif "empty" in order:
        if d:
            print(0)
        else:
            print(1)
    elif "front" in order:
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)

