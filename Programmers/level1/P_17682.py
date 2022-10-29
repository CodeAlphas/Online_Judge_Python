"""
 프로그래머스: [1차] 다트 게임 풀이
 Author: CodeAlphas
 Date: 2022/10/29
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/17682
 Version: Python 3.10.4
"""

def solution(dartResult):
    num = 0; s_num = ""; stages = [] 
    
    for i in range(len(dartResult)):
        s = dartResult[i]
        
        if s.isnumeric():
            s_num += s
            ch = True
        else:
            if ch:
                num = int(s_num)
                s_num = ""
                ch = False
                
            if s.isalpha():
                if s == 'S': squares = 1
                elif s == 'D': squares = 2
                else: squares = 3
                stages.append(num ** squares)
            else:
                if s == "*":
                    if len(stages) > 1:
                        for i in range(1, 3):
                            stages[-i] = 2 * stages[-i]
                    else:
                        stages[-1] = 2 * stages[-1]       
                else:
                    stages[-1] = -1 * stages[-1]

    return sum(stages)