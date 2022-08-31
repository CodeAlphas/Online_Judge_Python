"""
 백준 1024번: 수열의 합 풀이
 Author: CodeAlphas
 Date: 2022/08/31
 Problem Source: https://www.acmicpc.net/problem/1024
 Version: Python 3.10.4
"""

n, l = map(int, input().split())
ch = 0

def check(depth, len, num, sum_n, array):
    global ch

    if depth == len:
        if sum_n == n:
            print(*array)
            exit()
        elif sum_n > n:
            ch = -1
        else:
            ch = 0
        return

    check(depth+1, len, num+1, sum_n + num, array + [num])

for length in range(l, 101):
    start = n//length-length+2
    end = n//length+length

    if start < 0:
        start = 0

    for number in range(start, end):
        check(0, length, number, 0, [])
        if ch == -1:
            break
print(-1)