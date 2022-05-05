"""
 1546번: 평균
 Problem Source: https://www.acmicpc.net/problem/1546
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/04/19.
"""

n = int(input())
array = list(map(int, input().split()))
result = []
h_grade = max(array)

for i in array:
    result.append(i/h_grade*100)

print(sum(result)/n)

