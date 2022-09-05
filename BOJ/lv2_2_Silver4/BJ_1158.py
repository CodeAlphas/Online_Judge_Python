"""
 백준 1158번: 요세푸스 문제 풀이
 Author: CodeAlphas
 Date: 2022/09/05
 Problem Source: https://www.acmicpc.net/problem/1158
 Version: Python 3.10.4
"""

n, k = map(int, input().split())
list_n = list(i for i in range(1, n+1))

print("<", end = "")
index = 0
for i in range(n):
    index += k-1
    index %= len(list_n)
    if i == n-1:
        print(list_n.pop(index), end = ">")
    else:
        print(list_n.pop(index), end = ", ")