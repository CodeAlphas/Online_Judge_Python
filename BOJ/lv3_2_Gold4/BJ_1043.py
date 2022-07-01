"""
 백준 1043번: 거짓말 풀이
 Author: CodeAlphas
 Date: 2022/06/14
 Problem Source: https://www.acmicpc.net/problem/1043
 Version: Python 3.10.4
"""

# 1
# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split()) # 사람의 수, 파티의 수
# n_p, *p = list(map(int, input().split())) # 진실을 아는 사람의 수, 진실을 아는 사람의 번호

# party = []
# for i in range(m):
#     n_temp, *temp = list(map(int, input().split()))
#     party.append(temp)

# queue = deque(p); result = [1] * m; visited = [False] * 51

# while queue:
#     v = queue.popleft()
#     visited[v] = True

#     for i in range(m):
#         humans = party[i]
#         ch = False
#         for human in humans:
#             if visited[human]:
#                 result[i] = 0
#                 ch = True; break
#         if ch:
#             for human in humans:
#                 if not visited[human]:
#                     visited[human] = True
#                     queue.append(human)
                
# print(sum(result))

# 2
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 사람의 수, 파티의 수
p_t = set(map(int, input().split()[1:]))

party = []
for i in range(m):
    party.append(set(map(int, input().split()[1:])))

results = [1] * m
for _ in range(m):
    i = 0
    for participants in party:
        if participants.intersection(p_t):
            results[i] = 0; i += 1
            p_t = p_t.union(participants)

print(sum(results))