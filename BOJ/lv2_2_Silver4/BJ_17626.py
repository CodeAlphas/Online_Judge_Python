"""
 백준 17626번: Four Squares 풀이
 Author: CodeAlphas
 Date: 2022/06/11
 Problem Source: https://www.acmicpc.net/problem/17626
 Version: Python 3.10.4
"""

n = int(input())
m = int(n**0.5)+1

def check(n, m):
    a = n**0.5
    if a == int(a): return 1
    for i in range(1, m):
        b = (n-i**2)**0.5
        if b == int(b): return 2
    for i in range(1, m):
        for j in range(1, int((n-i**2)**0.5)+1):
            c = (n-i**2-j**2)**0.5
            if c == int(c): return 3
    return 4
    
print(check(n, m))

