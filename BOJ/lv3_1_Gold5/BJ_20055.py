"""
 백준 20055번: 컨베이어 벨트 위의 로봇 풀이
 Author: CodeAlphas
 Date: 2022/09/30
 Problem Source: https://www.acmicpc.net/problem/20055
 Version: Python 3.10.4
"""

# PyPy3 통과
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split())) 

belt = deque([[i, 0] for i in range(2 * n)]) 
count = 1 # 단계

def rotate():
    global belt

    belt.rotate(1)
    if belt[n-1][1] == 1:
        belt[n-1][1] = 0

def move(): 
    global a, belt

    for i in range(n-2, -1, -1):
        if belt[i][1] == 1:
            if belt[i+1][1] == 0 and a[belt[i+1][0]] >= 1: 
                belt[i+1][1] = belt[i][1] 
                belt[i][1] = 0
                a[belt[i+1][0]] -= 1

    if belt[n-1][1] == 1:
        belt[n-1][1] = 0

def check():
    c = 0
    for i in range(2 * n):
        if a[i] == 0: 
            c += 1
            if c >= k: return True
        
    return False

def load():
    if a[belt[0][0]] >= 1:
        belt[0][1] = 1 
        a[belt[0][0]] -= 1

while True:
    rotate()
    move()
    load()
    if check():
        break
    count += 1

print(count)