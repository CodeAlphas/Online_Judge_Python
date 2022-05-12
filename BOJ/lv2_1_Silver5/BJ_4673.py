"""
 백준 4673번: 셀프 넘버 풀이
 Author: CodeAlphas
 Date: 2022/04/22
 Problem Source: https://www.acmicpc.net/problem/4673
 Version: Python 3.10.4
"""

def d(n):
    result = 0
    nn = str(n)
    for i in range(len(nn)):
        result += int(nn[i])

    return n + result

array = []
for i in range(1, 10001):
    array.append(i)

darray = []
for j in range(1, 10001):
    temp = d(j)
    if temp <= 10000:
        darray.append(temp)

for k in set(darray): # set으로 중복값 제거
    array.remove(k)

for l in array:
    print(l)
