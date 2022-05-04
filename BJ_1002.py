"""
 1002번: 터렛
 Problem Source: https://www.acmicpc.net/problem/1002
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/05/04.
"""

# 1
# t = int(input())

# for test_case in range(1, t+1):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())

#     distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
#     enemy_dis = r1 + r2

#     if x1 == x2 and y1 == y2:
#         if r1 == r2:
#             print(-1)
#         else:
#             print(0)
#     else:
#         if distance > enemy_dis:
#             print(0)
#         elif distance < enemy_dis:
#             if abs(r2-r1) == distance:
#                 print(1)
#             elif r1 > distance + r2 or r2 > distance + r1:
#                 print(0)
#             else:
#                 print(2)
#         else:
#             print(1)

# 2
t = int(input())

for test_case in range(1, t+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5

    if x1 == x2 and y1 == y2 and r1 == r2: # 두 원이 겹칠 때
        print(-1)
    elif distance > r1 + r2 or distance + r1 < r2 or distance + r2 < r1: # 두 원이 서로 만나지 않을 때
        print(0)
    elif abs(r1 - r2) == distance or r1 + r2 == distance: # 두 원이 서로 내접, 외접할 때
        print(1)
    else:
        print(2)