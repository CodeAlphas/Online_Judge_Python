"""
 백준 2231번: 분해합 풀이
 Author: CodeAlphas
 Date: 2022/05/03
 Problem Source: https://www.acmicpc.net/problem/2231
 Version: Python 3.10.4
"""

n = int(input())
flag = True

for i in range(1, n):
    part_number = list(map(int, str(i))) # map은 리스트의 요소를 지정된 함수로 처리 해주는 함수
    sum_number = sum(part_number) + i

    if sum_number == n:
        print(i)
        flag = False
        break

if flag:
    print(0)