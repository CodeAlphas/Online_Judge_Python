"""
 프로그래머스: 위장 풀이
 Author: CodeAlphas
 Date: 2022/10/24
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42578
 Version: Python 3.10.4
"""

# 1
# def solution(clothes):
#     n = len(clothes)
#     clothes_ = []
#     result = 1
    
#     for i in range(n):
#         clothes_.append(clothes[i][1])
    
#     clothes_s = set(clothes_)
    
#     for j in clothes_s:
#         result *= (clothes_.count(j) + 1)

#     return result - 1

# 2
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth, ctype in clothes:
        if ctype in clothes_dict.keys():
            clothes_dict[ctype] += 1
        else:
            clothes_dict[ctype] = 1
    for value in clothes_dict.values():
        answer *= (value+1)
        
    return answer - 1