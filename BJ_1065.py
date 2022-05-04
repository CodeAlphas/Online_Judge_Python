"""
 1065번: 한수
 Problem Source: https://www.acmicpc.net/problem/1065
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/04/16.
"""

def CheckHansu(a):
    if 1 <= a <= 99:
        return True

    nn = str(a)
    i = 0
    while i+2 < len(nn):
        if int(nn[i+2]) - int(nn[i+1]) == int(nn[i+1]) - int(nn[i]):
            i += 1
            continue
        else:
            return False
    return True

n = int(input()) # 주어진 자연수 n
result = 0

for i in range(1, n+1):
    if CheckHansu(i):
        result += 1

print(result)