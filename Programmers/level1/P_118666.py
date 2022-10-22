"""
 프로그래머스: 성격 유형 검사하기 풀이
 Author: CodeAlphas
 Date: 2022/10/22
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/118666
 Version: Python 3.10.4
"""

def calculate(type1, type2, choice, ct_dict):
    if choice in [1, 2, 3]:
        ct_dict[type1] += (4-choice)
    elif choice in [5, 6, 7]:
        ct_dict[type2] += (choice-4)
    return ct_dict
    
def solution(survey, choices):
    answer = ''
    ct_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 
               'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        ct_dict = calculate(survey[i][0], survey[i][1], choices[i], ct_dict)
    
    ct = ['RT', 'CF', 'JM', 'AN']
    for i in range(4):
        if ct_dict[ct[i][0]] >= ct_dict[ct[i][1]]: 
            answer += ct[i][0]
        else:
            answer += ct[i][1]
    
    return answer