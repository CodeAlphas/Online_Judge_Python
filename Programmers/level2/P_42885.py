"""
 프로그래머스: 구명보트 풀이
 Author: CodeAlphas
 Date: 2022/11/05
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42885
 Version: Python 3.10.4
"""

def solution(people, limit):
    answer = 0
    people.sort()
    
    first = 0; last = len(people) - 1
    while first <= last:
        if people[first] + people[last] <= limit:
            first += 1
            last -= 1
        else:
            last -= 1
        answer += 1
            
    return answer