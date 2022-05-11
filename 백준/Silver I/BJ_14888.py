"""
 백준 14888번: 연산자 끼워넣기 풀이
 Author: CodeAlphas
 Date: 2022/04/18
 Problem Source: https://www.acmicpc.net/problem/14888
 Version: Python 3.10.4
"""

import copy
from itertools import permutations

n = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split()) # 1, 2, 3, 4
operators_ = []
results = []

for _ in range(plus):
    operators_.append(1)

for _ in range(minus):
    operators_.append(2)

for _ in range(mul):
    operators_.append(3)

for _ in range(div):
    operators_.append(4)

operators = set(permutations(operators_, n - 1)) # 중복 제거

for op in operators:
    a_t = copy.deepcopy(a)
    for i in range(n-1):
        if op[i] == 1:
            a_t[i+1] = (a_t[i] + a_t[i+1])
        elif op[i] == 2:
            a_t[i+1] = (a_t[i] - a_t[i+1])          
        elif op[i] == 3:
            a_t[i+1] = (a_t[i] * a_t[i+1])         
        elif op[i] == 4:
            a_t[i+1] = int(a_t[i] / a_t[i+1])       

    results.append(a_t[i+1])

print(max(results))
print(min(results)) 

