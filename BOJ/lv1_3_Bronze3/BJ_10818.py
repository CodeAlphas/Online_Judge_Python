"""
 백준 10818번: 최소, 최대 풀이
 Author: CodeAlphas
 Date: 2022/04/26
 Problem Source: https://www.acmicpc.net/problem/10818
 Version: Python 3.10.4
"""

# 1 
# n = int(input())
# array = list(map(int, input().split()))

# print(min(array), max(array))

# 2
n = int(input())
array = list(map(int, input().split()))

min_n = array[0]
max_n = array[0]

for i in array:
    if i < min_n:
        min_n = i
    if i > max_n:
        max_n = i

print(min_n, max_n)