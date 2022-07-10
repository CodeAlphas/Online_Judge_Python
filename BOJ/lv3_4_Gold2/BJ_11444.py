"""
 백준 11444번: 피보나치 수 6 풀이
 Author: CodeAlphas
 Date: 2022/06/20
 Problem Source: https://www.acmicpc.net/problem/11444
 Version: Python 3.10.4
"""

n = int(input())
matrix_a = [[1, 1], [1, 0]] # [[F_n+1, F_n], [F_n, F_n-1]] = [[1, 1], [1, 0]]^n

def fibonacci(n):
    if n == 0:
        return [[1, 0], [0, 1]]
    temp_matrix = fibonacci(n//2)
    if n % 2 == 0:
        return mul(temp_matrix, temp_matrix)  
    else:
        return mul(mul(temp_matrix, temp_matrix), matrix_a)

def mul(a, b):
    temp_a = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp_a[i][j] += a[i][k] * b[k][j]
            temp_a[i][j] %= 1000000007
    return temp_a

print(fibonacci(n)[0][1])