"""
 백준 1712번: 손익분기점 풀이
 Author: CodeAlphas
 Date: 2022/04/19
 Problem Source: https://www.acmicpc.net/problem/1712
 Version: Python 3.10.4
"""

a, b, c = map(int, input().split())

if c == b:
    print(-1)

else:
    n = int(a / (c-b)) 

    if n < 0: # n <= 0 아님
        print(-1)
    else:
        print(n+1)
