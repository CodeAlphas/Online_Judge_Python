"""
 백준 2798번: 블랙잭 풀이
 Author: CodeAlphas
 Date: 2022/05/03
 Problem Source: https://www.acmicpc.net/problem/2798
 Version: Python 3.10.4
"""

# 1
# n, m = map(int, input().split()) # 카드의 개수
# card_list = list(map(int, input().split())) 
# card_used = [False] * n # 사용한 카드 확인
# result = 0

# def solution(depth, sum_card):
#     global card_used
#     global result

#     if depth == 3:
#         if sum_card <= m:            
#             result = max(sum_card, result)
#         return
#     else:
#         size = len(card_list)
#         for i in range(size):
#             if card_used[i] != True:
#                 card_used[i] = True
#                 solution(depth + 1, sum_card + card_list[i])
#                 card_used[i] = False

# solution(0, 0)
# print(result)

# 2
from itertools import combinations

n, m = map(int, input().split()) # 카드의 개수
card_list = list(map(int, input().split())) 
result = 0

c_card = list(combinations(card_list, 3))

for card in c_card:
    a, b, c = card
    if a + b + c <= m:
        result = max(result, a+b+c)

print(result)