"""
 백준 11723번: 집합 풀이
 Author: CodeAlphas
 Date: 2022/06/03
 Problem Source: https://www.acmicpc.net/problem/11723
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    order = input().split()
    if "all" in order:
        s = {i for i in range(1, 21)}
    elif "empty" in order:
        s = set()
    elif "add" in order:
        s.add(int(order[1]))
    elif "remove" in order:
        s.discard(int(order[1]))
    elif "check" in order:
        if int(order[1]) in s:
            print(1)
        else:
            print(0)
    else:
        num = int(order[1])
        if num in s:
            s.remove(num)
        else:
            s.add(num)