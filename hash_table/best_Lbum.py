def solution(genres, plays):
    answer = []
    # print(plays)
    
    hash = {}
    for i, genre in enumerate(genres):
        if genre in hash:
            hash[genre].append((plays[i], i)) 
        else:
            hash[genre]= [(plays[i], i)]
    # print(hash)
    genre_cnt ={}
    for genre, song in hash.items():
        total_play = sum([play for play, idx in song])
        genre_cnt[genre] = total_play
        
    # 장르를 총 재생 횟수 기준으로 내림차순으로 정렬
    genre_sort = sorted(genre_cnt.items(), key=lambda x: x[1], reverse= True)
    # print(genre_sort)
    
    for genre, _ in genre_sort:
        # 장르 라는 것을 기준으로 인덱스 두개를 가져와야 함
        song_sort = sorted(hash[genre], key = lambda x:x[0], reverse = True)
        # print(song_sort)
        answer.append(song_sort[0][1])
        if len(song_sort) > 1:
            answer.append(song_sort[1][1])
                # answer.append([0])
#     print(f"{genre} 장르에서 가장 많이 재생된 노래들: {song_sort}")
    return answer