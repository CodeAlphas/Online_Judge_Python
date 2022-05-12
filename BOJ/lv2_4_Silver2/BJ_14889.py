"""
 백준 14889번: 스타트와 링크 풀이
 Author: CodeAlphas
 Date: 2022/04/19
 Problem Source: https://www.acmicpc.net/problem/14889
 Version: Python 3.10.4
"""

from itertools import combinations, permutations

n = int(input())
maps = []
teams = [i for i in range(n)]
skill_diff = 1e9

for _ in range(n):
    maps.append(list(map(int, input().split())))

a = n//2
teams_com = list(combinations(teams, a))

def solution():
    global skill_diff
    
    for tm in teams_com:
        skill1 = 0
        skill2 = 0

        teams_ = list(permutations(tm, 2))
        for x, y in teams_:
            skill1 += maps[x][y]

        tm1 = []
        for i in teams:
            if i not in tm:
                tm1.append(i)

        teams_ = list(permutations(tm1, 2))
        for x, y in teams_:
            skill2 += maps[x][y]
            
        skill_diff_t = abs(skill1 - skill2)
        skill_diff = min(skill_diff, skill_diff_t)

solution()    
print(skill_diff)