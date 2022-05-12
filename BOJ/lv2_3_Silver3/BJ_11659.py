"""
 백준 11659번: 구간 합 구하기 4 풀이
 Author: CodeAlphas
 Date: 2022/05/02
 Problem Source: https://www.acmicpc.net/problem/11659
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 수의 개수, 합을 구해야 하는 횟수
number_list = list(map(int, input().split()))
prefix_sum = [0]
sum_value = 0

for i in number_list:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(m):
    i, j = map(int, input().split())

    print(prefix_sum[j] - prefix_sum[i-1])