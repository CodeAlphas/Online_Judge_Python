"""
 백준 1107번: 리모컨 풀이
 Author: CodeAlphas
 Date: 2022/05/15
 Problem Source: https://www.acmicpc.net/problem/1107
 Version: Python 3.10.4
"""

# 1 PyPy3 통과, Python3 시간 초과
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input()) # 고장난 버튼의 개수
# ichannel = 100
# button = {str(i) for i in range(10)}
# results = int(10e9)
# n_len = len(str(n))

# if m != 0:
#     button -= set(input().split())
        
# def calculate(depth, channel, end):
#     global results

#     if depth == end:
#         if len(channel) != len(str(int(channel))):
#             c = len(str(int(channel)))
#         else:
#             c = end
#         results = min(results, c + abs(int(channel)-n))
#         return
        
#     else:
#         for i in button:
#             calculate(depth + 1, channel + i, end)

# if n_len >= 2:
#     calculate(0, "", n_len-1); calculate(0, "", n_len); calculate(0, "", n_len+1)
# else:
#     calculate(0, "", n_len); calculate(0, "", n_len+1)

# print(min(abs(n-ichannel), results))

# 2 PyPy3 통과, Python3 통과
import sys
input = sys.stdin.readline

n = int(input()) # 이동하려는 채널
m = int(input())
if m != 0:
    broken_button = input().split()
else:
    broken_button = []
result = int(1e9)

def checkChannel(ch):
    for bb in broken_button:
        if bb in str(ch):
            return False
    return True
        
for channel in range(0, 1000000):
    if checkChannel(channel):
        result = min(result, len(str(channel))+abs(channel-n))

print(min(result, abs(n-100)))
