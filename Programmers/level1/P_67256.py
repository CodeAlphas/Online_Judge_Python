"""
 프로그래머스: 키패드 누르기 풀이
 Author: CodeAlphas
 Date: 2022/10/19
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/67256
 Version: Python 3.10.4
"""

def check(number, l_pos, r_pos, hand):
    lx, ly = l_pos
    rx, ry = r_pos 
    if number == 0: x = 3; y = 1
    else: x = (number-2)//3; y = 1
    l_des = abs(lx-x) + abs(ly-y)
    r_des = abs(rx-x) + abs(ry-y)
    if l_des < r_des:
        return (x, y), r_pos, 'L'
    elif l_des > r_des:
        return l_pos, (x, y), 'R'
    else:
        if hand[0].upper() == 'R':
            return l_pos, (x, y), 'R'
        else:
            return (x, y), r_pos, 'L'

def solution(numbers, hand):
    answer = ''; l_pos = (3, 0); r_pos = (3, 2)
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            l_pos = ((number-1)//3, 0)
        elif number in [3, 6, 9]:
            answer += 'R'
            r_pos = (number//3-1, 2)
        else:
            l_pos, r_pos, ans = check(number, l_pos, r_pos, hand)
            answer += ans
    
    return answer