"""
 백준 2751번: 수 정렬하기 2 풀이
 Author: CodeAlphas
 Date: 2022/05/12
 Problem Source: https://www.acmicpc.net/problem/2751
 Version: Python 3.10.4
"""

# 1
# import sys
# input = sys.stdin.readline

# def mergeSort(list):
#     list_len = len(list)
#     if list_len <= 1:
#         return list

#     mid = list_len//2
#     left_list = mergeSort(list[:mid])
#     right_list = mergeSort(list[mid:])
#     merge_list = []

#     idx1 = 0; idx2 = 0

#     while idx1 < len(left_list) and idx2 < len(right_list):
#         if left_list[idx1] < right_list[idx2]:
#             merge_list.append(left_list[idx1])
#             idx1 += 1
#         else:
#             merge_list.append(right_list[idx2])
#             idx2 += 1

#     if idx1 == len(left_list):
#         merge_list += right_list[idx2:]
#     else:
#         merge_list += left_list[idx1:]

#     return merge_list

# n = int(input())
# array = []

# for _ in range(n):
#     array.append(int(input()))

# merged_list = mergeSort(array)

# for i in merged_list:
#     print(i)

# 2
# import sys
# input = sys.stdin.readline

# def mergeSort(list):
#     list_len = len(list)
#     if list_len <= 1:
#         return list

#     mid = list_len//2
#     left_list = mergeSort(list[:mid])
#     right_list = mergeSort(list[mid:])

#     idx1 = 0; idx2 = 0; idx3 = 0

#     while idx1 < len(left_list) and idx2 < len(right_list):
#         if left_list[idx1] < right_list[idx2]:
#             list[idx3] = left_list[idx1]
#             idx1 += 1; idx3 += 1
#         else:
#             list[idx3] = right_list[idx2]
#             idx2 += 1; idx3 += 1

#     while idx1 < len(left_list):
#         list[idx3] = left_list[idx1]
#         idx1 += 1; idx3 += 1
#     while idx2 < len(right_list):
#         list[idx3] = right_list[idx2]
#         idx2 += 1; idx3 += 1

#     return list

# n = int(input())
# array = []

# for _ in range(n):
#     array.append(int(input()))

# merged_list = mergeSort(array)

# for i in merged_list:
#     print(i) 

# 3
import sys
input = sys.stdin.readline

def mergeSort(list):
    list_len = len(list)
    if list_len <= 1:
        return list

    mid = list_len//2
    left_list = mergeSort(list[:mid])
    right_list = mergeSort(list[mid:])

    idx1 = 0; idx2 = 0; idx3 = 0
    left_len = len(left_list); right_len = len(right_list)

    while idx1 < left_len and idx2 < right_len:
        if left_list[idx1] < right_list[idx2]:
            list[idx3] = left_list[idx1]
            idx1 += 1; idx3 += 1
        else:
            list[idx3] = right_list[idx2]
            idx2 += 1; idx3 += 1

    while idx1 < left_len:
        list[idx3] = left_list[idx1]
        idx1 += 1; idx3 += 1
    while idx2 < right_len:
        list[idx3] = right_list[idx2]
        idx2 += 1; idx3 += 1

    return list

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

merged_list = mergeSort(array)

for i in merged_list:
    print(i)