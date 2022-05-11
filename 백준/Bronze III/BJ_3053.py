"""
 백준 3053번: 택시 기하학 풀이
 Author: CodeAlphas
 Date: 2022/05/04
 Problem Source: https://www.acmicpc.net/problem/3053
 Version: Python 3.10.4
"""

from math import pi

def u_area(r):
    return pi * r * r

def nu_area(r):
    return 2 * r * r

r = int(input())
print("%.6f" %u_area(r))
print("%.6f" %nu_area(r))