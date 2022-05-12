"""
 백준 2750번: 수 정렬하기 풀이
 Author: CodeAlphas
 Date: 2022/05/03
 Problem Source: https://www.acmicpc.net/problem/2750
 Version: Python 3.10.4
"""

def bubbleSort(A):
    size = len(A)
    for i in range(size):
        for j in range(1, size-i):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]

n = int(input())
array = []

for _ in range(n):  
    array.append(int(input()))

bubbleSort(array)
num = len(array)

for i in range(num):
    print(array[i])