"""
 백준 10973번: 이전 순열 풀이
 Author: CodeAlphas
 Date: 2022/08/26
 Problem Source: https://www.acmicpc.net/problem/10973
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
first_seq = [i for i in range(1, n+1)]

if seq == first_seq:
    print(-1)
else:
    index = 1
    for i in range(n - 1, 0, -1):
        if seq[i-1] > seq[i]:
            index = i
            break
    for j in range(n - 1, 0, -1):
        if seq[index-1] > seq[j]:
            seq[index-1], seq[j] = seq[j], seq[index-1]
            print(*(seq[:index] + sorted(seq[index:], reverse=True)))
            exit()