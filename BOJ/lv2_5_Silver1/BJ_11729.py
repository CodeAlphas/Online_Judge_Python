"""
 백준 11729번: 하노이 탑 이동 순서 풀이
 Author: CodeAlphas
 Date: 2022/07/11
 Problem Source: https://www.acmicpc.net/problem/11729
 Version: Python 3.10.4
"""

n = int(input())

result = 2**n - 1
print(result)

def check(n, start, end):
    if n == 0:
        return
    else:
        check(n-1, start, 6 - start - end)
        print(start, end)
        check(n-1, 6 - start - end, end)
        
check(n, 1, 3)