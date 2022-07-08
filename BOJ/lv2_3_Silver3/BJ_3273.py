"""
 백준 3273번: 두 수의 합 풀이
 Author: CodeAlphas
 Date: 2022/06/18
 Problem Source: https://www.acmicpc.net/problem/3273
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
array = sorted(list(map(int, input().split())))
x = int(input())

count = 0
start, end = 0, n - 1

while start < end:
    temp_sum = array[start] + array[end]
    if temp_sum == x:
        start += 1; end -= 1
        count += 1
    elif temp_sum > x:
        end -= 1
    elif temp_sum < x:
        start += 1

print(count)