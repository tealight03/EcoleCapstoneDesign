from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def can_transform(word1, word2):
        return sum(1 for a, b in zip(word1, word2) if a != b) == 1

    queue = deque([(begin, 0)])  # (현재 단어, 변환 단계)
    visited = set()

    while queue:
        current, steps = queue.popleft()

        if current == target:
            return steps

        for word in words:
            if word not in visited and can_transform(current, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0