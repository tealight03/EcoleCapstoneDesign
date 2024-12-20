from collections import defaultdict

def solution(genres, plays):
    # 장르별 총 재생 횟수와 곡별 재생 횟수를 저장
    genre_play_count = defaultdict(int)
    songs = defaultdict(list)

    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        songs[genre].append((play, i))

    # 장르별로 정렬
    sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)

    answer = []
    for genre in sorted_genres:
        # 각 장르에서 곡을 재생 횟수와 고유 번호로 정렬 (내림차순, 고유 번호는 오름차순)
        sorted_songs = sorted(songs[genre], key=lambda x: (-x[0], x[1]))
        # 상위 두 곡을 추가
        answer.extend([idx for _, idx in sorted_songs[:2]])

    return answer