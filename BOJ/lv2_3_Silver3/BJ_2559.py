"""
 백준 2559번: 수열 풀이
 Author: CodeAlphas
 Date: 2022/07/24
 Problem Source: https://www.acmicpc.net/problem/2559
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))
sum_num = sum(array[:k])
result = sum_num

for i in range(1, n-k+1):
    sum_num += array[i+k-1]
    sum_num -= array[i-1]
    result = max(result, sum_num)

print(result)