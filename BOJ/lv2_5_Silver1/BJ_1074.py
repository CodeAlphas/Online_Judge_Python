"""
 백준 1074번: Z 풀이
 Author: CodeAlphas
 Date: 2022/05/21
 Problem Source: https://www.acmicpc.net/problem/1074
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
result = -1

def solution(x, y, cn):
    global result
    
    if cn == 1:
        result += 1
        if x == r and y == c:
            print(result)
        return
    elif not (x <= r < x + cn and y <= c < y + cn):
        result += cn * cn
        return
    
    div = cn // 2
    solution(x, y, div)
    solution(x, y + div, div)
    solution(x + div, y, div)
    solution(x + div, y + div, div)

solution(0, 0, 2 ** n)