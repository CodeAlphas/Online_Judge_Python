"""
 백준 10809번: 알파벳 찾기 풀이
 Author: CodeAlphas
 Date: 2022/04/27
 Problem Source: https://www.acmicpc.net/problem/10809
 Version: Python 3.10.4
"""

s = input()
alphabet = list(range(97, 123))

for i in alphabet:
    print(s.find(chr(i)), end = " ")