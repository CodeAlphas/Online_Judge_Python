"""
 백준 9012번: 괄호 풀이
 Author: CodeAlphas
 Date: 2022/05/08
 Problem Source: https://www.acmicpc.net/problem/9012
 Version: Python 3.10.4
"""

t = int(input())

for _ in range(t):
    vps = input()
    vps_len = len(vps)
    stack = []

    for i in range(vps_len):
        if stack:
            if stack[-1] == '(':
                if vps[i] == '(':
                    stack.append(vps[i])
                elif vps[i] == ')':
                    stack.pop()
            elif stack[-1] == ')':
                stack.append(vps[i])
        else:
            stack.append(vps[i])

    if stack:
        print("NO")
    else:
        print("YES")           

