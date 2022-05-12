"""
 백준 18870번: 좌표 압축 풀이
 Author: CodeAlphas
 Date: 2022/05/07
 Problem Source: https://www.acmicpc.net/problem/18870
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))
sort_list = sorted(list(set(num_list)))
sl_len = len(sort_list)
rdict = {}

for i in range(sl_len):
    rdict[sort_list[i]] = i 

for num in num_list:
    print(rdict[num], end = ' ') 

