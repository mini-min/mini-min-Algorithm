def solution(genres, plays):
    genre_play_dict = {}
    song_list = []
    answer = []

    # 장르별 재생횟수 합을 받는 딕셔너리 -> 많은 재생횟수 순으로 정렬
    for i, j in zip(genres,plays):
        if i in genre_play_dict:
            genre_play_dict[i] += j
        else:
            genre_play_dict[i] = j
    sortsum = sorted(genre_play_dict.items(), key=lambda x:x[1], reverse=True)
    
    # song_list 생성 -> "[인덱스, 장르, 플레이]" 순으로 저장 -> 플레이 횟수를 기준으로 정렬
    for ind, (genre, play) in enumerate(zip(genres, plays)):
        song_list.append([ind, genre, play])
    song_list = sorted(song_list, key=lambda x:x[2], reverse=True)
    
    # 인덱스를 최종 반환 리스트에 추가
    for genre, _ in sortsum:
        count = 0
        for i in song_list:
            if count == 2: break        # 카운트 2개까지만 저장
            if i[1] == genre:
                answer.append(i[0])     # 인덱스를 리스트에 저장
                count += 1
    
    return answer
