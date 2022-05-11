"""
 백준 1181번: 단어 정렬 풀이
 Author: CodeAlphas
 Date: 2022/05/06
 Problem Source: https://www.acmicpc.net/problem/1181
 Version: Python 3.10.4
"""

n = int(input())
words = []
words_legth = [[] for _ in range(51)]

for _ in range(n):
    words.append(input())

words = list(set(words))

for wo in words:
    a = len(wo)
    words_legth[a].append((a, wo))

for i in words_legth:
    if i != []:
        length = len(i)
        if length == 1:
            print(i[0][1])
        else:
            i.sort()
            for j in range(length):
                print(i[j][1])




