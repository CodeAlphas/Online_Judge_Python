"""
 프로그래머스: 베스트앨범 풀이
 Author: CodeAlphas
 Date: 2022/09/20
 Problem Source: https://school.programmers.co.kr/learn/courses/30/lessons/42579
 Version: Python 3.10.4
"""

def solution(genres, plays):
    answer = []
    
    num = len(genres)
    genres_dict = {}; songs_dict = {}
    for i in range(num):
        if genres[i] not in genres_dict.keys():
            genres_dict[genres[i]] = plays[i]
            songs_dict[genres[i]] = [(plays[i], -i)]
        else:
            genres_dict[genres[i]] += plays[i]
            songs_dict[genres[i]].append((plays[i], -i))
            
    sorted_dict = sorted(genres_dict.items(), key = lambda item: item[1], reverse = True)
    for genre in sorted_dict:
        temp = sorted(songs_dict[genre[0]], key = lambda item: (item[0], item[1]), reverse = True)
        if len(temp) >= 2:
            answer.append(-temp[0][1])
            answer.append(-temp[1][1])
        else:
            answer.append(-temp[0][1])
    
    return answer