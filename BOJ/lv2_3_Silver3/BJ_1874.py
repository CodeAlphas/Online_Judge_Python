"""
 백준 1874번: 스택 수열 풀이
 Author: CodeAlphas
 Date: 2022/05/19
 Problem Source: https://www.acmicpc.net/problem/1874
 Version: Python 3.10.4
"""

# 1 PyPy3만 통과
# import sys
# input = sys.stdin.readline

# n = int(input())
# check = [True for _ in range(0, n+1)]
# sequece = []
# for i in range(n):
#     sequece.append(int(input()))
# stack = []
# results = []

# for i in range(n):
#     seq = sequece[i]

#     if check[seq] == False:
#         if stack:
#             try:
#                 while stack[-1] != seq:
#                     stack.pop()
#                     results.append("-")
#                 stack.pop()
#                 results.append("-")
#             except:
#                 results = ["NO"]
#                 break 
#         else:
#             results = ["NO"]
#             break
#     elif check[seq] == True:
#         for j in range(1, seq+1):
#             if check[j] == True:
#                 check[j] = False
#                 stack.append(j)
#                 results.append("+")
#         stack.pop()
#         results.append("-")        

# print("\n".join(results))

# 2 PyPy3, Python 3 모두 통과 
import sys
input = sys.stdin.readline

n = int(input())
stack = []; results = []; sequece = []
for i in range(n):
    sequece.append(int(input()))
last = 0

for i in range(n):
    while last < sequece[i]:
        last += 1
        stack.append(last)
        results.append("+")

    if stack[-1] == sequece[i]:
        stack.pop()
        results.append("-")
    else:
        results = ["NO"]
        break
    
print("\n".join(results))