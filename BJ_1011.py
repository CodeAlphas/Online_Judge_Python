"""
 1011번: Fly me to the Alpha Centauri
 Problem Source: https://www.acmicpc.net/problem/1011
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/05/04.
"""

# 재귀적 해결은 0 <= x < y < 2^31 이라는 조건상 maximum recursion depth exceeded 에러가 날 수 있다.

t = int(input())

for test_case in range(1, t+1):
    x, y = map(int, input().split())
    distance = y - x

    i = 0; n = 1; check = 0
    while True:
        if i >= distance:
            break
        i += n
        check += 1
        if check % 2 == 0:
            n += 1
        
    if check % 2 == 0:
        print(2 * (n - 1))
    else:
        print(2 * n - 1)



    








