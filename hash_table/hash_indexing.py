gener = ["classic", "pop", "classic", "classic", "pop"]
play = [500, 600, 150, 800, 2500]

# 장르별 재생 횟수를 저장할 딕셔너리
genre_play_count = {}

# enumerate를 사용해 gener 리스트의 인덱스와 값을 함께 순회
for i, genre in enumerate(gener):
    if genre in genre_play_count:
        genre_play_count[genre] += play[i]  # 해당 장르의 재생 횟수를 더함
    else:
        genre_play_count[genre] = play[i]  # 처음 등장한 장르는 새로 추가

# 결과 출력
print(genre_play_count)

# {
#     "classic": 1450,
#     "pop": 3100
# }


# 장르별로 (재생 횟수, 인덱스)의 리스트를 저장할 딕셔너리
genre_play_index = {}

# enumerate를 사용하여 gener와 play를 엮음
for i, genre in enumerate(gener):
    if genre in genre_play_index:
        genre_play_index[genre].append((play[i], i))  # 재생 횟수와 인덱스를 함께 저장
    else:
        genre_play_index[genre] = [(play[i], i)]

# 결과 출력
print(genre_play_index)

# {
#     "classic": [(500, 0), (150, 2), (800, 3)],
#     "pop": [(600, 1), (2500, 4)]
# }

# 장르별로 가장 많이 재생된 노래를 찾기 위해 정렬
for genre, songs in genre_play_index.items():
    # 재생 횟수 기준으로 내림차순 정렬
    songs_sorted = sorted(songs, key=lambda x: x[0], reverse=True)
    print(f"{genre} 장르에서 가장 많이 재생된 노래들: {songs_sorted}")
    
    # classic 장르에서 가장 많이 재생된 노래들: [(800, 3), (500, 0), (150, 2)]
    # pop 장르에서 가장 많이 재생된 노래들: [(2500, 4), (600, 1)]
