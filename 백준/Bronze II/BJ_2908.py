"""
 백준 2908번: 상수 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2908
 Version: Python 3.10.4
"""

# 1
# a, b = input().split()

# a = int(a[2] + a[1] + a[0])
# b = int(b[2] + b[1] + b[0])

# if a > b:
#     print(a)
# else:
#     print(b)

# 2
a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

if a > b:
    print(a)
else:
    print(b)