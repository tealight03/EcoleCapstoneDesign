def solution(s):
    def compress(length):
        compressed = ""
        count = 1
        prev = s[:length]

        for i in range(length, len(s), length):
            current = s[i:i + length]
            if prev == current:
                count += 1
            else:
                compressed += (str(count) + prev) if count > 1 else prev
                prev = current
                count = 1

        compressed += (str(count) + prev) if count > 1 else prev
        return len(compressed)

    if len(s) == 1:
        return 1

    return min(compress(length) for length in range(1, len(s) // 2 + 1))