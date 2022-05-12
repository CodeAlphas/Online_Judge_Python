"""
 백준 10814번: 나이순 정렬 풀이
 Author: CodeAlphas
 Date: 2022/05/09
 Problem Source: https://www.acmicpc.net/problem/10814
 Version: Python 3.10.4
"""

# 1
# import sys
# input = sys.stdin.readline

# n = int(input())
# members_list = []

# for _ in range(n):
#     age, name = input().split()
#     members_list.append((int(age), name))

# members_list.sort(key=lambda a:a[0])

# for age, name in members_list:
#     print(age, name)

# 2
import sys
input = sys.stdin.readline

n = int(input())
members_list = [[] for _ in range(201)]

for _ in range(n):
    age, name = input().split()
    members_list[int(age)].append((age, name))

for i in range(201):
    if members_list[i] != []:
        for age, name in members_list[i]:
            print(age, name)