"""
 백준 13458번: 시험 감독 풀이
 Author: CodeAlphas
 Date: 2022/04/29
 Problem Source: https://www.acmicpc.net/problem/13458
 Version: Python 3.10.4
"""

# 1
# n = int(input())
# a = list(map(int, input().split()))
# b, c = map(int, input().split())
# supervisor_su = 0

# if b > c:
#     for i in range(n):
#         a[i] -=  b
#         supervisor_su += 1 # 총 감독
#         if a[i] % c != 0:
#             supervisor_su += ((a[i] // c) + 1) # 부 감독
#         else:
#             supervisor_su += (a[i] // c) # 부 감독
# else:
#     for i in range(n):
#         if a[i] % c != 0:
#             # if (a[i] % c) == b:
#             supervisor_su += ((a[i] // c) + 1) # 부 감독
#         else:
#             supervisor_su += (a[i] // c) # 부 감독

# print(supervisor_su)

# 2
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
supervisor_su = 0

for i in range(n):
    a[i] = a[i] - b
    supervisor_su += 1
    if a[i] <= 0: # 음수가 되지 않도록 주의
        continue
    if a[i] % c != 0:
        supervisor_su += ((a[i] // c) + 1) # 부 감독
    else:
        supervisor_su += (a[i] // c) # 부 감독

print(supervisor_su)

