from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
            node.count += 1

    def search(self, query):
        node = self.root
        for char in query:
            if char == "?":
                return node.count
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

def solution(words, queries):
    # 정방향 및 역방향 트라이 생성
    tries = defaultdict(Trie)
    reversed_tries = defaultdict(Trie)

    for word in words:
        length = len(word)
        tries[length].insert(word)
        reversed_tries[length].insert(word[::-1])

    answer = []
    for query in queries:
        length = len(query)
        if query[0] != "?":
            answer.append(tries[length].search(query))
        else:
            answer.append(reversed_tries[length].search(query[::-1]))

    return answer