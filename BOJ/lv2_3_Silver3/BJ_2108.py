"""
 백준 2108번: 통계학 풀이
 Author: CodeAlphas
 Date: 2022/05/10
 Problem Source: https://www.acmicpc.net/problem/2108
 Version: Python 3.10.4
"""

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
numbers = []
max_counts = 0
max_numbers_list = []

for _ in range(n):
    numbers.append(int(input()))

sum_numbers = sum(numbers)
if sum_numbers >= 0:
    print(int(sum(numbers)/n+0.5)) # 산술 평균
else:
    print(int(sum(numbers)/n-0.5))

numbers.sort()
print(numbers[n//2]) # 중앙값

c_numbers = Counter(numbers).most_common()

if len(c_numbers) == 1:
    print(c_numbers[0][0]) # 최빈값
else:
    if c_numbers[0][1] == c_numbers[1][1]:
        print(c_numbers[1][0])
    else:
        print(c_numbers[0][0])

print(numbers[-1] - numbers[0]) # 최댓값과 최솟값의 차이

