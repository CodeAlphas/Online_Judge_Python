"""
 백준 2775번: 부녀회장이 될테야 풀이
 Author: CodeAlphas
 Date: 2022/05/02
 Problem Source: https://www.acmicpc.net/problem/2775
 Version: Python 3.10.4
"""

t = int(input()) # 테스트 케이스 수

for test_case in range(1, t+1):
    k = int(input()) # 층 수
    n = int(input()) # 호 수

    apartment = [[] * (k+1)]
    for i in range(1, n+1):
        apartment[0].append(i)

    for j in range(1, k+1):
        temp = 0
        apartment.append([])
        for l in range(0, n):
            temp += apartment[j-1][l]
            apartment[j].append(temp)

    print(apartment[k][n-1])


