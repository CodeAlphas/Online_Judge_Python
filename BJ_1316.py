"""
 1316번: 그룹 단어 체커
 Problem Source: https://www.acmicpc.net/problem/1316
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/04/19.
"""

import sys
input = sys.stdin.readline

n = int(input())
count = 0

for i in range(n):
    temp = []
    s = input()

    for j in s:
        if j not in temp:
            temp.append(j)
            a = j
            continue
        else:
            if j == a:
                continue
            else:
                count -= 1
                break
    count += 1

print(count)