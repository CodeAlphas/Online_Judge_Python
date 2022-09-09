"""
 백준 25501번: 재귀의 귀재 풀이
 Author: CodeAlphas
 Date: 2022/09/09
 Problem Source: https://www.acmicpc.net/problem/25501
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

t = int(input())

def recursion(s, l, r, num):
    if l >= r: 
        return 1, num
    elif s[l] != s[r]:
        return 0, num
    else:
        return recursion(s, l+1, r-1, num+1)

def is_palindrome(s):
    return recursion(s, 0, len(s)-1, 1)

for _ in range(t):
    s = input().rstrip()
    a, b = is_palindrome(s)
    print(a, b)