"""
 백준 9498번: 시험 성적 풀이
 Author: CodeAlphas
 Date: 2022/04/18
 Problem Source: https://www.acmicpc.net/problem/9498
 Version: Python 3.10.4
"""

jumsu = int(input())

if jumsu >= 90:
    print("A")
elif jumsu >= 80:
    print("B")
elif jumsu >= 70:
    print("C")
elif jumsu >= 60:
    print("D")
else:
    print("F")