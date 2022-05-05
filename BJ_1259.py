"""
 1259번: 팰린드롬수 
 Problem Source: https://www.acmicpc.net/problem/1259
 Version: Python 3.10.4

 Created by CodeAlphas on 2022/05/04.
"""

while True:
    n = input()
    if int(n) == 0:
        break
    
    length = len(n)
    flag = False

    for i in range(length//2 + 1):
        if n[i] == n[length-i-1]:
            continue
        else:
            flag = True
            break

    if flag:
        print("no")
    else:
        print("yes")