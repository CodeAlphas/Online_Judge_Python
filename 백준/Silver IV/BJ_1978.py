"""
 백준 1978번: 소수 찾기 풀이
 Author: CodeAlphas
 Date: 2022/04/20
 Problem Source: https://www.acmicpc.net/problem/1978
 Version: Python 3.10.4
"""

# int 함수는 실수의 소수점 아래를 제거해서 반환한다.
n = int(input()) # 주어진 수의 개수
find_list = list(map(int, input().split())) # 주어진 수
result = 0 # 소수의 개수

for number in find_list:
    if number != 1:
        result += 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            result -= 1
            break

print(result)