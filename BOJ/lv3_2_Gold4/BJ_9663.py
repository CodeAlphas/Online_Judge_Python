"""
 백준 9663번: N-Queen 풀이
 Author: CodeAlphas
 Date: 2022/07/05
 Problem Source: https://www.acmicpc.net/problem/9663
 Version: Python 3.10.4
"""

n = int(input())
count = 0
array = [0] * n

def solution(array, row):
    global count

    if row == n:
        count += 1
        return
    else:
        for col in range(n):
            array[row] = col
            for x in range(row):
                if array[x] == array[row] or abs(array[x]-array[row]) == abs(row - x): 
                    break
            else:
                solution(array, row+1)

solution(array, 0)
print(count)
