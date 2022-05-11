"""
 백준 11047번: 동전 0 풀이
 Author: CodeAlphas
 Date: 2022/05/02
 Problem Source: https://www.acmicpc.net/problem/11047
 Version: Python 3.10.4
"""

n, k = map(int, input().split()) # 동전 종류, 동전을 적절히 사용해 만드는 가치의 합
coin_list = []
result = 0

for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list.sort(reverse = True)

for co in coin_list:
    if k >= co:
        result += k // co
        k %= co

print(result)