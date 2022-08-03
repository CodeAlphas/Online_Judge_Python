"""
 백준 13305번: 주유소 풀이
 Author: CodeAlphas
 Date: 2022/07/14
 Problem Source: https://www.acmicpc.net/problem/13305
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
path = list(map(int, input().split()))
prices = list(map(int, input().split()))

sum_road = path[0]; price = prices[0]; result = 0
for i in range(1, n-1):
    if price <= prices[i]:
        sum_road += path[i]
    else:
        result += price * sum_road
        price = prices[i]
        sum_road = path[i]
result += price * sum_road

print(result)