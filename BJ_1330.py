"""
 1330번: 두 수 비교하기
 Problem Source: https://www.acmicpc.net/problem/1330
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/04/19.
"""

a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")