"""
 백준 2630번: 색종이 만들기 풀이
 Author: CodeAlphas
 Date: 2022/06/01
 Problem Source: https://www.acmicpc.net/problem/2630
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())

papers = []
for _ in range(n):
    papers.append(list(map(int, input().split())))

whites = 0; blues = 0

def check(s_x, s_y, n):
    global whites, blues
    temp = papers[s_x][s_y]
    for i in range(s_x, s_x + n):
        for j in range(s_y, s_y + n):
            if temp != papers[i][j]:
                check(s_x, s_y, n//2)
                check(s_x + n//2, s_y, n//2)
                check(s_x, s_y + n//2, n//2)
                check(s_x + n//2, s_y + n//2, n//2)
                return
            else:
                temp = papers[i][j]

    if temp == 1:
        blues += 1
    else:
        whites += 1
    return
            
check(0, 0, n)
print(whites)
print(blues)
        
            