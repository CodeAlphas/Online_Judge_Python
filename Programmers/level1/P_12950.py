"""
 프로그래머스: 행렬의 덧셈 풀이
 Author: CodeAlphas
 Date: 2022/11/17
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/12950
 Version: Python 3.10.4
"""

def solution(arr1, arr2):
    answer = []
    n, m = len(arr1), len(arr1[0])
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
        
    return answer