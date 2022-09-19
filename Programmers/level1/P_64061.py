"""
 프로그래머스: 크레인 인형뽑기 게임 풀이
 Author: CodeAlphas
 Date: 2022/09/19
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/64061
 Version: Python 3.10.4
"""

def solution(board, moves):
    answer = 0; basket = [0]
    n = len(board)
    
    for num in moves:
        num -= 1
        for i in range(n):
            if board[i][num] != 0:
                if basket[-1] == board[i][num]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board[i][num])
                board[i][num] = 0
                break

    return answer