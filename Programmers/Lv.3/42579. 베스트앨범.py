"""
미완
def solution(genres, plays):
    answer = []
    hash_dict = {}
    total_play = {}
    
    # 딕셔너리에 "장르: [재생횟수, 인덱스]" 형태로 저장
    for i in range(len(genres)):
        if genres[i] not in hash_dict:
            hash_dict[genres[i]] = [[plays[i], i]]
        else:
            hash_dict[genres[i]].append([plays[i], i])
    
    print(hash_dict)
    
    for genre in hash_dict:
        hash_dict[genre].sort(reverse=True)
        print(hash_dict)
        sum = 0
        for element in range(len(hash_dict[genre])):
            sum += hash_dict[genre][element][0]
        total_play[genre] = sum

    #print(total_play)
    
    for i in sorted(total_play, reverse=True):
        if len(hash_dict[i]) == 1:
            answer.append(ash_dict[i][0][1])
        else:
            answer.append(hash_dict[i][0][1])
            answer.append(hash_dict[i][1][1])
    
    return answer
"""
