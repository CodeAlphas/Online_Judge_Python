"""
 프로그래머스: 여행경로 풀이
 Author: CodeAlphas
 Date: 2022/10/05
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/43164
 Version: Python 3.10.4
"""

answers = []

def dfs(start, answer, dict_tickets, tickets):
    global answers
    
    if start in dict_tickets and dict_tickets[start] != []:
        for _ in range(len(dict_tickets[start])):
            temp = dict_tickets[start].pop()
            dfs(temp, answer + [temp], dict_tickets, tickets)
            dict_tickets[start].insert(0, temp)
    else:
        if len(answer) == len(tickets) + 1: answers.append(answer)
        return
    
def solution(tickets):
    answer = ["ICN"]; dict_tickets = {}
    for start, end in tickets:
        dict_tickets[start] = dict_tickets.get(start, []) + [end]
    for key in dict_tickets.keys():
        dict_tickets[key].sort(reverse = True)
        
    dfs("ICN", answer, dict_tickets, tickets)
    return answers[0]