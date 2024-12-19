def solution(s):
    def convert_word(word):
        # 각 단어를 변환: 짝수 인덱스 -> 대문자, 홀수 인덱스 -> 소문자
        return ''.join(
            c.upper() if i % 2 == 0 else c.lower()
            for i, c in enumerate(word)
        )

    # 문자열을 단어별로 나누어 변환 후 다시 합치기
    return ' '.join(convert_word(word) for word in s.split(' '))