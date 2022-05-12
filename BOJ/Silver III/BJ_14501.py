"""
 백준 14501번: 퇴사 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/14501
 Version: Python 3.10.4
"""

n = int(input())
sangdam = []
don = 0
dons = []
do = [0, 1]

for i in range(n):
    t, p = map(int, input().split())
    sangdam.append((t, p))

def solution(depth, don, skip):

    if depth == n + 1:
        dons.append(don)
        return 

    for i in range(len(do)):
        if do[i] == 1:
            if depth > skip and depth + sangdam[depth-1][0] - 1 <= n:
                don += sangdam[depth-1][1]
                skip = depth + sangdam[depth-1][0] - 1
        solution(depth + 1, don, skip)

solution(1, 0, -1)
print(max(dons))
