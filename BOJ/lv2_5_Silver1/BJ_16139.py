"""
 백준 16139번: 인간-컴퓨터 상호작용 풀이
 Author: CodeAlphas
 Date: 2022/08/23
 Problem Source: https://www.acmicpc.net/problem/16139
 Version: Python 3.10.4
"""

# PyPy3만 통과
import sys
input = sys.stdin.readline

s = input().rstrip()
q = int(input())

alphabet_num = [[0] * 26 for _ in range(len(s))]
for i in range(len(s)):
    alphabet_num[i][ord(s[i])-97] = 1

    if i == 0:
        continue
    else:
        for j in range(26):
            alphabet_num[i][j] += alphabet_num[i-1][j]

for _ in range(q):
    a, l, r = input().split()
    l = int(l); r = int(r)

    if l == 0:
        print(alphabet_num[r][ord(a)-97])
    else:
        print(alphabet_num[r][ord(a)-97] - alphabet_num[l-1][ord(a)-97])