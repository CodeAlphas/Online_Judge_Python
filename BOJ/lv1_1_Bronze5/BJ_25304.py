"""
 백준 25304번: 영수증 풀이
 Author: CodeAlphas
 Date: 2022/09/08
 Problem Source: https://www.acmicpc.net/problem/25304
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
costs = 0

for _ in range(n):
    item, num = map(int, input().split())
    costs += item * num

if costs == x:
    print("Yes")
else:
    print("No")