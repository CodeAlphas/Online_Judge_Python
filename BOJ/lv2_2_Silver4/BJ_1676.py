"""
 백준 1676번: 팩토리얼 0의 개수 풀이
 Author: CodeAlphas
 Date: 2022/05/26
 Problem Source: https://www.acmicpc.net/problem/1676
 Version: Python 3.10.4
"""

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input())
num = str(factorial(n))
len_num = len(num)

count = 0
for i in range(len_num-1, -1, -1):

    if num[i] == '0':
        count += 1
    else:
        break

print(count)
