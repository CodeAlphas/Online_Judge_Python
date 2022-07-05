"""
 백준 1780번: 종이의 개수 풀이
 Author: CodeAlphas
 Date: 2022/06/17
 Problem Source: https://www.acmicpc.net/problem/1780
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
minus_one = 0; zero = 0; one = 0
paper = []

for _ in range(n):
    paper.append(list(map(int, input().split())))

def check(x, y, p):
    global minus_one, zero, one

    if p == 0:
        return

    temp = paper[x][y]; ch = False
    for i in range(x, x+p):
        for j in range(y, y+p):
            if temp == paper[i][j]:
                continue
            else:
                ch = True
                break
        if ch:
            check(x, y, p//3)
            check(x+p//3, y, p//3)
            check(x+2*p//3, y, p//3)
            check(x, y+p//3, p//3)
            check(x+p//3, y+p//3, p//3)
            check(x+2*p//3, y+p//3, p//3)
            check(x, y+2*p//3, p//3)
            check(x+p//3, y+2*p//3, p//3)
            check(x+2*p//3, y+2*p//3, p//3)
            break

    if not ch:
        if temp == -1:
            minus_one += 1
        elif temp == 0:
            zero += 1
        else:
            one += 1

check(0, 0, n)
print(minus_one)
print(zero)
print(one)