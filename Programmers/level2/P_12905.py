"""
 프로그래머스: 가장 큰 정사각형 찾기 풀이
 Author: CodeAlphas
 Date: 2022/10/23
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12905
 Version: Python 3.10.4
"""

def solution(board):
    m, n = len(board), len(board[0])
    
    dp = [[0] * n for _ in range(m)]
    dp[0] = board[0]
    for i in range(m):
        dp[i][0] = board[i][0]
    
    side = dp[0][0]
    for x in range(1, m):
        for y in range(1, n):
            if board[x][y] == 1:
                dp[x][y] = min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1]) + 1
                side = max(side, dp[x][y])
        
    return side ** 2