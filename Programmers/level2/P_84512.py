"""
 프로그래머스: 모음사전 풀이
 Author: CodeAlphas
 Date: 2022/11/01
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/84512
 Version: Python 3.10.4
"""

def check(word, temp, depth):
    global answer, t_answer

    t_answer += 1
    if temp == word:
        answer = t_answer
        return
    elif depth == 5:
        return
    else:
        for a in ['A', 'E', 'I', 'O', 'U']:
            check(word, temp + a, depth + 1)

t_answer = -1; answer = 0
def solution(word):
    check(word, "", 0)
    return answer