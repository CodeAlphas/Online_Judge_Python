"""
 백준 9095번: 1, 2, 3 더하기 풀이
 Author: CodeAlphas
 Date: 2022/05/22
 Problem Source: https://www.acmicpc.net/problem/9095
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())

def check(number):
    global result

    if number == n:
        result += 1
        return
    elif number >= n:
        return

    for i in range(1, 4):
        check(number + i)
    

for test_case in range(0, t):
    result = 0
    n = int(input())

    check(0)
    print(result)