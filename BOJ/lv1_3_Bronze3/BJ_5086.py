"""
 백준 5086번: 배수와 약수 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/5086
 Version: Python 3.10.4
"""

a, b = map(int, input().split())
while a != 0 and b != 0:
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
    a, b = map(int, input().split())