"""
 백준 1992번: 쿼드트리 풀이
 Author: CodeAlphas
 Date: 2022/06/10
 Problem Source: https://www.acmicpc.net/problem/1992
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
maps = []; result = []
for _ in range(n):
    maps.append(list(input().rstrip()))

def check(x1, y1, n):
    global result
    if n == 0:
        return
    else:
        temp = maps[x1][y1]; ch = True
        for i in range(x1, x1+n):
            for j in range(y1, y1+n):
                if maps[i][j] == temp == '1':
                    ch = True
                elif maps[i][j] == temp == '0':
                    ch = False
                else:
                    result.append('(')
                    check(x1, y1, n//2)
                    check(x1, y1+n//2, n//2)
                    check(x1+n//2, y1, n//2)
                    check(x1+n//2, y1+n//2, n//2)
                    result.append(')')
                    return
        if ch:
            result.append('1')
        else:
            result.append('0')

check(0, 0, n)
print(''.join(result))

