"""
 백준 1920번: 수 찾기 풀이
 Author: CodeAlphas
 Date: 2022/05/07
 Problem Source: https://www.acmicpc.net/problem/1920
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
list_n = list(map(int, input().split()))
dic_n = {}
len_n = len(list_n)
for i in range(len_n):
    dic_n[list_n[i]] = i

print(dic_n)
m = int(input())
list_m = list(map(int, input().split()))

for i in range(m):
    if list_m[i] in dic_n:
        print(1)
    else:
        print(0)



