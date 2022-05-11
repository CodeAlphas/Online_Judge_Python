"""
 백준 9610번: 사분면 풀이
 Author: CodeAlphas
 Date: 2022/04/15
 Problem Source: https://www.acmicpc.net/problem/9610
 Version: Python 3.10.4
"""

n = int(input())
q1, q2, q3, q4, axis = 0, 0, 0, 0, 0

for i in range(n):
    x, y = map(int, input().split())
    if x > 0:
        if y > 0:
            q1 += 1
        elif y < 0:
            q4 += 1
        else:
            axis += 1
    elif x < 0:
        if y > 0:
            q2 += 1
        elif y < 0:
            q3 += 1
        else:
            axis += 1
    else:
        axis += 1

print("Q1: %d" %q1)
print("Q2: %d" %q2)
print("Q3: %d" %q3)
print("Q4: %d" %q4)
print("AXIS: %d" %axis)
