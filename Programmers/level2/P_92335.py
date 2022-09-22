"""
 프로그래머스: k진수에서 소수 개수 구하기 풀이
 Author: CodeAlphas
 Date: 2022/09/22
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/92335
 Version: Python 3.10.4
"""

def isPrime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

def solution(n, k):
    answer = 0; num = ""; t_num = ""
    
    while n != 0:
        num += str(n % k)
        n //= k
    ln = len(num)
    num = num[-1:-ln-1:-1] + "0"
    
    for i in range(ln+1):
        if num[i] != "0":
            t_num += num[i]
        else:
            if t_num != "" and isPrime(int(t_num)):
                print(t_num)
                answer += 1
            t_num = ""
            
    return answer