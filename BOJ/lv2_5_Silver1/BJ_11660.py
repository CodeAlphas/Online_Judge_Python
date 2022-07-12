"""
 백준 11660번: 구간 합 구하기 5 풀이
 Author: CodeAlphas
 Date: 2022/06/22
 Problem Source: https://www.acmicpc.net/problem/11660
 Version: Python 3.10.4
"""

# 1. PyPy3만 통과
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# graph = []
# for i in range(1, n+1):
#     graph += list(map(int, input().split()))

# dp = [0]; tp_sum = 0
# for i in graph:
#     tp_sum += i
#     dp.append(tp_sum)
    
# for _ in range(m):
#     result = 0
#     x1, y1, x2, y2 = map(int, input().split())
#     a = x1-1; b = x2
#     for i in range(a, b):
#         result += (dp[i*n+y2] - dp[i*n+y1-1])
    
#     print(result)

# 2
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[0] * (n+1)]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())))

dp = [[0]* (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = graph[i][j] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] 

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])
