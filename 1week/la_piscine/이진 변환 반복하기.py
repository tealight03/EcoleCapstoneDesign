def solution(s):
    binary_conversion_count = 0
    removed_zero_count = 0

    while s != "1":
        # 0 제거
        removed_zero_count += s.count("0")
        s = s.replace("0", "")

        # 길이를 2진수로 변환
        s = bin(len(s))[2:]
        binary_conversion_count += 1

    return [binary_conversion_count, removed_zero_count]