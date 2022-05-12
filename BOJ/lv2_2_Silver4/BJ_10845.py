"""
 백준 10845번: 큐 풀이
 Author: CodeAlphas
 Date: 2022/05/05
 Problem Source: https://www.acmicpc.net/problem/10845
 Version: Python 3.10.4
"""

# 1 
# import sys
# input = sys.stdin.readline

# n = int(input())
# queue = []

# for _ in range(n):
#     order = input().split()
#     length = len(order)
#     size = len(queue)
#     if length == 2:
#         queue.append(order[1])
#     else:
#         if order[0] == "pop":
#             if size != 0:
#                 print(queue[0])
#                 queue.remove(queue[0])
#             else:
#                 print(-1)
#         elif order[0] == "size":
#             print(size)
#         elif order[0] == "empty":
#             if size == 0:
#                 print(1)
#             else:
#                 print(0)
#         elif order[0] == "front":
#             if size == 0:
#                 print(-1)
#             else:
#                 print(queue[0])
#         else:
#             if size == 0:
#                 print(-1)
#             else:
#                 print(queue[-1])

# 2
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    order = input().split()
    length = len(order)
    size = len(queue)

    if length == 2:
        queue.append(order[1])
    else:
        if order[0] == "pop":
            if size != 0:
                print(queue.popleft())
            else:
                print(-1)
        elif order[0] == "size":
            print(size)
        elif order[0] == "empty":
            if size == 0:
                print(1)
            else:
                print(0)
        elif order[0] == "front":
            if size == 0:
                print(-1)
            else:
                print(queue[0])
        else:
            if size == 0:
                print(-1)
            else:
                print(queue[-1])