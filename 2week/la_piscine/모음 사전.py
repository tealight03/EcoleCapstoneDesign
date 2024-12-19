def solution(word):
    from itertools import product

    # 가능한 모든 단어 생성
    vowels = ['A', 'E', 'I', 'O', 'U']
    all_words = []

    for i in range(1, 6):  # 단어 길이: 1부터 5까지
        for p in product(vowels, repeat=i):
            all_words.append(''.join(p))

    # 사전 순 정렬
    all_words.sort()

    # 입력 단어의 위치 반환
    return all_words.index(word) + 1