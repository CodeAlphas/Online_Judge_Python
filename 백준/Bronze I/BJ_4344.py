"""
 백준 4344번: 평균은 넘겠지 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/4344
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

c = int(input())
a = 0

for i in range(c):
    array = list(map(int, input().split()))
    array.pop(0)

    avg = sum(array)/len(array)

    for j in array:
        if j > avg:
            a += 1
    print("%.3f%%" %(a/len(array) * 100)) # %% -> %
    a = 0
