"""
 백준 9935번: 문자열 폭발 풀이
 Author: CodeAlphas
 Date: 2022/06/28
 Problem Source: https://www.acmicpc.net/problem/9935
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

s = input().rstrip(); len_s = len(s)
find_s = input().rstrip(); len_find_s = len(find_s)
stack = []

for i in range(len_s):
    if s[i] == find_s[-1]:
        if "".join(stack[-len_find_s+1:]) == find_s[:-1]:
            for _ in range(len_find_s-1):
                stack.pop()
        elif len_find_s != 1:
            stack.append(s[i])
    else:
        stack.append(s[i])

if stack:
    print("".join(stack))
else:
    print("FRULA")