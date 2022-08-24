"""
 백준 1021번: 회전하는 큐 풀이
 Author: CodeAlphas
 Date: 2022/08/24
 Problem Source: https://www.acmicpc.net/problem/1021
 Version: Python 3.10.4
"""

from collections import deque

n, m = map(int, input().split())
pos_list = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])
result = 0

for pos in pos_list:
    cur_pos = queue.index(pos) + 1
    len_queue = len(queue)
    if len_queue - cur_pos + 1> cur_pos - 1:
        result += (cur_pos - 1)
        queue.rotate(-cur_pos + 1)
        queue.popleft()
    else:
        result += (len_queue - cur_pos + 1)
        queue.rotate(len_queue - cur_pos + 1)
        queue.popleft()

print(result)