"""
 백준 24060번: 알고리즘 수업 - 병합 정렬 1 풀이
 Author: CodeAlphas
 Date: 2022/09/10
 Problem Source: https://www.acmicpc.net/problem/24060
 Version: Python 3.10.4
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))
count = 0; ans = -1

def merge_sort(p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(p, q)
        merge_sort(q+1, r)
        merge(p, q, r)

def merge(p, q, r):
    global array, count, ans
    
    i = p; j = q + 1
    
    tmp = []
    while i <= q and j <= r:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    while i <= q:
        tmp.append(array[i])
        i += 1
    while j <= r:
        tmp.append(array[j])
        j += 1

    i = p; t = 0
    while i <= r:
        count += 1
        if count == k:
            ans = tmp[t]
        array[i] = tmp[t]
        i += 1; t += 1

merge_sort(0, len(array)-1)
print(ans)