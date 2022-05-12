"""
 백준 2577번: 숫자의 개수 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2577
 Version: Python 3.10.4
"""

# 1
# a = int(input())
# b = int(input())
# c = int(input())
# num = str(a * b * c)

# for i in range(10):
#     print(num.count(str(i)))

# 2
a = int(input())
b = int(input())
c = int(input())
num = list(str(a * b * c))

for i in range(10):
    print(num.count(str(i)))
