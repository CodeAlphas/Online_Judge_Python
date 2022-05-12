"""
 백준 1018번: 체스판 다시 칠하기 풀이
 Author: CodeAlphas
 Date: 2022/05/03
 Problem Source: https://www.acmicpc.net/problem/1018
 Version: Python 3.10.4
"""

# 1
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# maps = [[[] for _ in range(m)] for _ in range(n)]
# results = int(1e10)

# for i in range(n):
#     temp = input()
#     for j in range(m):
#         maps[i][j] = temp[j]

# for i in range(n-7):
#     for k in range(m-7):
#         temp = 0
#         for j in range(i, i+8):
#             for l in range(k, k+8):
#                 if j % 2 == 0:
#                     if l % 2 == 0:
#                         if maps[j][l] == "W":
#                             temp += 1
#                     else:
#                         if maps[j][l] == "B":
#                             temp += 1
#                 else:
#                     if l % 2 == 0:
#                         if maps[j][l] == "B":
#                             temp += 1
#                     else:
#                         if maps[j][l] == "W":
#                             temp += 1
#         results = min(results, temp)

# for i in range(n-7):
#     for k in range(m-7):
#         temp = 0
#         for j in range(i, i+8):
#             for l in range(k, k+8):
#                 if j % 2 == 0:
#                     if l % 2 == 0:
#                         if maps[j][l] == "B":
#                             temp += 1
#                     else:
#                         if maps[j][l] == "W":
#                             temp += 1
#                 else:
#                     if l % 2 == 0:
#                         if maps[j][l] == "W":
#                             temp += 1
#                     else:
#                         if maps[j][l] == "B":
#                             temp += 1
#         results = min(results, temp)

# print(results)

# 2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [[[] for _ in range(m)] for _ in range(n)]
results = int(1e10)

for i in range(n):
    temp = input()
    for j in range(m):
        maps[i][j] = temp[j]

for i in range(n-7):
    for k in range(m-7):
        temp_w = 0
        temp_b = 0
        for j in range(i, i+8):
            for l in range(k, k+8):
                if j % 2 == 0:
                    if l % 2 == 0:
                        if maps[j][l] == "W": # 시작이 "B"
                            temp_b += 1
                        else:
                            temp_w += 1
                    else:
                        if maps[j][l] == "B":
                            temp_b += 1
                        else:
                            temp_w += 1
                else:
                    if l % 2 == 0:
                        if maps[j][l] == "B":
                            temp_b += 1
                        else:
                            temp_w += 1    
                    else:
                        if maps[j][l] == "W":
                            temp_b += 1
                        else:
                            temp_w += 1    
        results = min(results, temp_b, temp_w)

print(results)


