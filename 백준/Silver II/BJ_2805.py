"""
 백준 2805번: 나무 자르기 풀이
 Author: CodeAlphas
 Date: 2022/05/04
 Problem Source: https://www.acmicpc.net/problem/2805
 Version: Python 3.10.4
"""

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split()) # 나무의 수, 집으로 가져가려고 하는 나무의 길이
# trees = list(map(int, input().split()))
# start, end = 0, max(trees) 

# while start <= end:
#     tree = 0
#     mid = (start + end) // 2 # 절단기 높이

    # for tr in trees:
    #     if tr > mid:
    #         tree += tr-mid

#     if tree >= m:
#         start = mid + 1
#     else:
#         end = end - 1

# print(end)

import sys
input = sys.stdin.readline

def binary_search(start, end):
    while start <= end:
        tree = 0
        mid = (start + end) // 2 # 절단기 높이

        for tr in trees:
            if tr > mid:
                tree += tr-mid

        if tree >= m:
            start = mid + 1
        else:
            end = mid - 1
    return end

n, m = map(int, input().split()) # 나무의 수, 집으로 가져가려고 하는 나무의 길이
trees = list(map(int, input().split()))
start, end = 0, max(trees) 

print(binary_search(start, end))