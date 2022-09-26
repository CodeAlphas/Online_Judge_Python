"""
 프로그래머스: 큰 수 만들기 풀이
 Author: CodeAlphas
 Date: 2022/09/26
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42883
 Version: Python 3.10.4
"""

def solution(number, k):
    result = ""
    number = list(map(int, list(number)))
    len_n = len(number)
    
    n = len(number) - k; it = n; i = 0
    for _ in range(it):
        part_number = number[i:len_n-n+1]
        max_num = 0; max_index = 0; index = 0
        for num in part_number:
            if num == 9: max_num = num; max_index = index; break
            if num > max_num: max_num = num; max_index = index
            index += 1
        result += str(max_num)
        i = max_index + i + 1
        n -= 1
        
    return result