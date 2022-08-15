"""
 백준 1269번: 대칭 차집합 풀이
 Author: CodeAlphas
 Date: 2022/07/26
 Problem Source: https://www.acmicpc.net/problem/1269
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

a, b = map(int, input().split())
list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

dict_a = {}
for num in list_a:
    dict_a[num] = 1

count = 0
for num in list_b:
    if num in dict_a:
        count += 1

print(a+b-2*count)