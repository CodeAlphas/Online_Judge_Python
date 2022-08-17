"""
 백준 12904번: A와 B 풀이
 Author: CodeAlphas
 Date: 2022/08/13
 Problem Source: https://www.acmicpc.net/problem/12904
 Version: Python 3.10.4
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
result = 0

def check_string(s, t, length_s, length_t):
    global result 

    if length_s == length_t:
        if s == t:
            result = 1
            return 
        else:
            return 

    if t[-1] == "A":
        check_string(s, t[:-1], length_s, length_t-1)
    elif t[-1] == "B":
        check_string(s, (t[:-1])[::-1], length_s, length_t-1)

check_string(s, t, len(s), len(t))
print(result)