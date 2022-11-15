"""
 프로그래머스: 하노이의 탑 풀이
 Author: CodeAlphas
 Date: 2022/11/15
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12946
 Version: Python 3.10.4
"""

def hanoi(answer, n, origin, destin, layover):
    if n == 1:
        answer.append([origin, destin])
        return
    else:
        hanoi(answer, n-1, origin, layover, destin)
        answer.append([origin, destin])
        hanoi(answer, n-1, layover, destin, origin)

def solution(n):
    answer = []
    hanoi(answer, n, 1, 3, 2)
    return answer