"""
 백준 5525번: IOIOI 풀이
 Author: CodeAlphas
 Date: 2022/05/23
 Problem Source: https://www.acmicpc.net/problem/5525
 Version: Python 3.10.4
"""

# 1 50점
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# s = input()
# pattern = "I" + "OI" * n
# result = 0

# index = -2
# while True:
#     index += 2
#     if pattern in s[index:]:
#         index = s.find(pattern, index)
#         result += 1
#     else:
#         break

# print(result)

# 2 100점
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
pattern_ = 0
result = 0
index = 1

while index < m-1:
    if s[index-1] == "I" and s[index] == "O" and s[index+1] == "I":
        pattern_ += 1
        if pattern_ == n:
            result += 1
            pattern_ -= 1
        index += 2
    else:
        pattern_ = 0
        index += 1

print(result)