"""
 백준 15596번: 정수 N개의 합 풀이
 Author: CodeAlphas
 Date: 2022/04/14
 Problem Source: https://www.acmicpc.net/problem/15596
 Version: Python 3.10.4
"""

def solve(a: list):
    result = 0
    for i in a:
        result += i
    return result