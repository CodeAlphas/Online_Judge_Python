"""
 백준 10250번: ACM 호텔 풀이
 Author: CodeAlphas
 Date: 2022/04/23
 Problem Source: https://www.acmicpc.net/problem/10250
 Version: Python 3.10.4
"""

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split()) # 층수, 각 층의 방 수, 손님 번호
    if n <= h:
        first = n % (h+1)
        print(first*100 + 1)
    else:
        first = n % h
        second = n // h + 1
        if first == 0:
            first = h
            second -= 1
        print(first*100 + second)

