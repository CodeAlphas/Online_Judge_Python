"""
 백준 2869번: 달팽이는 올라가고 싶다 풀이
 Author: CodeAlphas
 Date: 2022/04/21
 Problem Source: https://www.acmicpc.net/problem/2869
 Version: Python 3.10.4
"""

# 1
# a, b, v = map(int, input().split())

# n = (v-a) // (a-b)

# if n * (a-b) + a < v:
#     print(n+2)
# else:
#     print(n+1)

# 2
# ceil() 함수는 주어진 숫자보다 크거나 같은 가장 가까운 정수를 찾아주는 함수
import math

a, b, v = map(int, input().split())

n = math.ceil((v-b) / (a-b))
print(n)

