"""
 백준 5622번: 다이얼 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/5622
 Version: Python 3.10.4
"""

# 1
# a = input().lower()
# result = 0

# for i in range(len(a)):
#     if a[i] in ['a', 'b', 'c']:
#         result += 3
#     elif a[i] in ['d', 'e', 'f']:
#         result += 4
#     elif a[i] in ['g', 'h', 'i']:
#         result += 5
#     elif a[i] in ['j', 'k', 'l']:
#         result += 6
#     elif a[i] in ['m', 'n', 'o']:
#         result += 7
#     elif a[i] in ['p', 'q', 'r', 's']:
#         result += 8
#     elif a[i] in ['t', 'u', 'v']:
#         result += 9
#     elif a[i] in ['w', 'x', 'y', 'z']:
#         result += 10

# print(result)

# 2
a = input().lower()
result = 0
array = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

for i in a:
    for j in array:
        if i in j:
            result += (array.index(j) + 3)

print(result)
