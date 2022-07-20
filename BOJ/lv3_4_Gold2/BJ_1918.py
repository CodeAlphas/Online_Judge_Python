"""
 백준 1918번: 후위 표기식 풀이
 Author: CodeAlphas
 Date: 2022/06/29
 Problem Source: https://www.acmicpc.net/problem/1918
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

x = input().rstrip()

def infixToPostfix(x):
    len_x = len(x); stack = []; result = []
    prior = {"(" : 0, "+" : 1, "-" : 1, "*" : 2, "/" : 2}

    for i in range(len_x):
        if x[i].isalpha():
            result.append(x[i])
        else:
            if x[i] == ")":
                while stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            elif x[i] == "(":
                stack.append(x[i])
            else:
                if stack:
                    while stack:
                        if prior[stack[-1]] < prior[x[i]]:
                            stack.append(x[i]); break
                        else:
                            result.append(stack.pop())
                    if not stack:
                        stack.append(x[i])
                else:
                    stack.append(x[i])
    while stack:
        result.append(stack.pop())

    return result

print("".join(infixToPostfix(x)))