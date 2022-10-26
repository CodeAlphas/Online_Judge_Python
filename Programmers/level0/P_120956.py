"""
 프로그래머스: 옹알이 풀이
 Author: CodeAlphas
 Date: 2022/10/26
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/120956
 Version: Python 3.10.4
"""

def solution(babbling):
    poss = ["aya", "ye", "woo", "ma"]
    imposs = list(map(lambda x : x*2, poss))
    for i in range(len(babbling)):
        for j in range(4):
            if imposs[j] in babbling[i]: 
                break
            elif poss[j] in babbling[i]:
                babbling[i] = babbling[i].replace(poss[j], ' ')
        babbling[i] = babbling[i].replace(' ', '')
    
    return babbling.count('')