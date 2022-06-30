"""
 백준 15650번: N과 M (2) 풀이
 Author: CodeAlphas
 Date: 2022/06/14
 Problem Source: https://www.acmicpc.net/problem/15650
 Version: Python 3.10.4
"""

# 1
# from itertools import combinations

# n, m = map(int, input().split())
# array = [i for i in range(1, n+1)]

# result = list(combinations(array, m))
# for i in result:
#     for j in i:
#         print(j, end = ' ')
#     print()

# 2
n, m = map(int, input().split())

def solution(array, x):
    if len(array) == m:
        print(*array)
        return
    else:
        for i in range(x, n+1):
            if i not in array:
                array.append(i)
                solution(array, i+1)
                array.pop()

solution([], 1)