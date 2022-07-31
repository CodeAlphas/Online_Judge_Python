"""
 백준 11478번: 서로 다른 부분 문자열의 개수 풀이
 Author: CodeAlphas
 Date: 2022/07/12
 Problem Source: https://www.acmicpc.net/problem/11478
 Version: Python 3.10.4
"""

s = input()
s_len = len(s)
parts_s = {}

for i in range(1, s_len+1):
    for j in range(0, s_len-i+1):
        parts_s[s[j:j+i]] = 1

print(len(parts_s.keys()))