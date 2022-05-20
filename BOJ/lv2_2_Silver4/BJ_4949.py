"""
 백준 4949번: 균형잡힌 세상 풀이
 Author: CodeAlphas
 Date: 2022/05/18
 Problem Source: https://www.acmicpc.net/problem/4949
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

input_list = input().rstrip()

while input_list != ".":
    stack = []

    for st in input_list:
        if st == "(" or st == "[":
            stack.append(st)
        elif st == ")":
            if stack:
                peek = stack[-1]
            else:
                stack.append(st)
                break
            if peek == "(":
                stack.pop()
                continue
            else:
                break
        elif st == "]":
            if stack:
                peek = stack[-1]
            else:
                stack.append(st)
                break
            if peek == "[":
                stack.pop()
                continue
            else:
                break

    if stack:
        print("no")
    else:
        print("yes")
                
    input_list = input().rstrip()