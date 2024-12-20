# 4week(1018)

### 강의 내용
<a href="https://velog.io/@davin0706/Ecole-%EC%BA%A1%EC%8A%A4%ED%86%A4-%EB%94%94%EC%9E%90%EC%9D%B8-4%EC%A3%BC%EC%B0%A8" target="_blank">
<img src="https://github.com/user-attachments/assets/f78f04d5-7ed9-4645-92fb-0b8064d6a651" width="800"><br>
Click here to move!</a>

### La Piscine
<ul>
  <li>
    <b>1. 순위</b><br><br>
    <img src="https://github.com/user-attachments/assets/f120ce9b-ed25-4a5a-8f8c-0dd2cf516189" width="1000"><br><br>

    def solution(n, results):
    # 그래프 초기화
    wins = [[False] * (n + 1) for _ in range(n + 1)]

    # 결과 입력
    for winner, loser in results:
        wins[winner][loser] = True

    # 플로이드-워셜 알고리즘 적용
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if wins[i][k] and wins[k][j]:
                    wins[i][j] = True

    # 각 선수의 승패 기록을 확인
    answer = 0
    for i in range(1, n + 1):
        known_results = 0
        for j in range(1, n + 1):
            if wins[i][j] or wins[j][i]:
                known_results += 1

        if known_results == n - 1:
            answer += 1

    return answer
  </li>
  <li>
    <b>2. 길찾기 게임</b><br><br>
    <img src="https://github.com/user-attachments/assets/27575ea3-42aa-44db-9bc9-c778fdff8bf7" width="1000"><br><br>

    import sys
    sys.setrecursionlimit(10**6) # 런타임에러 방지
    
    # Tree 클래스 생성하기
    class Tree:
        def __init__(self):
            self.parent = None
            self.left = None
            self.right = None
            self.data = None
            self.index = None
    
    # 전위순회
    def preOrder(root, vector):
        if root == None:
            return vector
            
        vector.append(root.index)
        preOrder(root.left,vector)
        preOrder(root.right,vector)
            
        return vector
        
    # 후위순회
    def postOrder(root, vector):
    
        if root == None:
            return vector
        postOrder(root.left, vector)
        postOrder(root.right, vector)
        vector.append(root.index)
    
        return vector
    
    def solution(nodeinfo):
        # 이진 트리에 데이터 저장
        root = None
        
        for i in range(len(nodeinfo)):
            nodeinfo[i].append(i+1)
            
        # y좌표를 기준으로 내림차순 정렬
        nodeinfo = sorted(nodeinfo, key= lambda x:x[1], reverse=True)
        
        # enumerate 함수로 for문 반복
        for i,node in enumerate(nodeinfo):
            newTree = Tree()
            newTree.index = node[2]
            newTree.data = node
            
            if root == None:
                root = newTree
            else:
                curTree = root
                
                while 1:
                    # 새로 삽입하려는 데이터가 원래 데이터보다 크다면 오른쪽에 삽입
                    if curTree.data[0] < newTree.data[0]:
                        # 현재 노드의 오른쪽 노드가 null이라면
                        if curTree.right == None:
                            curTree.right = newTree
                            newTree.parent = curTree
                            break
                        # 현재 노드의 오른쪽 노드를 현재 노드로 다시 정의한다
                        else:
                            curTree = curTree.right
                            
                    # 새로 삽입하려는 데이터가 원래 데이터보다 작다면 왼쪽에 삽입
                    else:
                        # 현재 노드의 왼쪽 노드가 null이라면
                        if curTree.left == None:
                            curTree.left = newTree
                            newTree.parent = curTree
                            break
                        # 현재 노드의 왼쪽 노드를 현재 노드로 다시 정의한다
                        else:
                            curTree = curTree.left
    
        # 최종 순회 후 결과값을 저장
        answer = [preOrder(root,[]), postOrder(root,[])]
        return answer
  </li>
  <li>
    <b>3. 디스크 컨트롤러</b><br><br>
    <img src="https://github.com/user-attachments/assets/0262cc0a-102e-408a-8e50-818ea73a2213)" width="1000"><br><br>

    import heapq

    def solution(jobs):
        jobs.sort()  # 요청 시간 순으로 정렬
        heap = []
        time = 0  # 현재 시간
        index = 0  # jobs의 인덱스
        total_time = 0  # 요청부터 종료까지의 총 시간 합
    
        while index < len(jobs) or heap:
            # 현재 시간까지 요청된 작업을 힙에 추가
            while index < len(jobs) and jobs[index][0] <= time:
                heapq.heappush(heap, (jobs[index][1], jobs[index][0]))  # (소요 시간, 요청 시간)
                index += 1
    
            if heap:
                # 소요 시간이 가장 짧은 작업을 처리
                duration, request_time = heapq.heappop(heap)
                time += duration
                total_time += time - request_time
            else:
                # 힙이 비어 있으면 다음 작업의 요청 시간으로 점프
                time = jobs[index][0]
    
        return total_time // len(jobs)
  </li>
  <li>
    <b>4. 보석 쇼핑</b><br><br>
    <img src="https://github.com/user-attachments/assets/1181489e-6491-4ccc-8b8c-04644717f60c" width="1000"><br><br>

    from collections import defaultdict

    def solution(gems):
        gem_types = len(set(gems))  # 보석의 종류 수
        gem_count = defaultdict(int)  # 현재 구간의 보석 개수
    
        start, end = 0, 0
        shortest = float('inf')  # 최소 구간 길이
        answer = [0, 0]  # 결과 구간
    
        while end < len(gems):
            gem_count[gems[end]] += 1
            end += 1
    
            # 모든 보석을 포함한 구간인지 확인
            while len(gem_count) == gem_types:
                if end - start < shortest:
                    shortest = end - start
                    answer = [start + 1, end]  # 1-indexed 결과 저장
    
                # 구간의 시작점 보석 제거
                gem_count[gems[start]] -= 1
                if gem_count[gems[start]] == 0:
                    del gem_count[gems[start]]
                start += 1
    
        return answer
  </li>
  <li>
    <b>5. 섬 연결하기</b><br><br>
    <img src="https://github.com/user-attachments/assets/e76fb891-b323-4360-971f-14f5a5a1535d" width="1000"><br><br>

    def solution(n, costs):
    # 간선을 가중치 기준으로 정렬
    costs.sort(key=lambda x: x[2])

    # 각 노드의 부모를 저장 (Union-Find)
    parent = [i for i in range(n)]

    # 부모를 찾는 함수
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])  # 경로 압축
        return parent[node]

    # 두 노드를 합치는 함수
    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            parent[root2] = root1

    total_cost = 0

    # 최소 스패닝 트리 생성
    for node1, node2, cost in costs:
        if find(node1) != find(node2):
            union(node1, node2)
            total_cost += cost

    return total_cost
  </li>
  <li>
    <b>6. 가사 검색[통과 X]</b><br><br>
    <img src="https://github.com/user-attachments/assets/b05544c8-4664-47c2-bf53-033d6a908da4" width="1000"><br><br>

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
  </li>
  <li>
    <b>7. 키패드 누르기</b><br><br>
    <img src="https://github.com/user-attachments/assets/0cfa3161-cc3b-462d-bc89-f74cc883f937" width="1000"><br><br>

    def solution(numbers, hand):
    # 키패드 위치 정의
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    # 현재 위치 초기화
    left_pos = keypad['*']
    right_pos = keypad['#']

    result = []

    for number in numbers:
        if number in [1, 4, 7]:
            result.append('L')
            left_pos = keypad[number]
        elif number in [3, 6, 9]:
            result.append('R')
            right_pos = keypad[number]
        else:
            # 거리 계산
            target_pos = keypad[number]
            left_dist = abs(left_pos[0] - target_pos[0]) + abs(left_pos[1] - target_pos[1])
            right_dist = abs(right_pos[0] - target_pos[0]) + abs(right_pos[1] - target_pos[1])

            if left_dist < right_dist:
                result.append('L')
                left_pos = target_pos
            elif right_dist < left_dist:
                result.append('R')
                right_pos = target_pos
            else:
                if hand == "right":
                    result.append('R')
                    right_pos = target_pos
                else:
                    result.append('L')
                    left_pos = target_pos

    return ''.join(result)
  </li>
  <li>
    <b>8. 2개 이하로 다른 비트</b><br><br>
    <img src="https://github.com/user-attachments/assets/2d9658da-9db6-4940-9ab4-d9b4e0eef1c1" width="1000"><br><br>

    def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            # 짝수인 경우, +1 하면 비트가 하나만 달라짐
            answer.append(number + 1)
        else:
            # 홀수인 경우, 가장 오른쪽에서 처음 등장하는 0을 1로 바꾸고
            # 그 다음 비트를 0으로 바꾼다
            binary = list('0' + bin(number)[2:])  # 앞에 '0' 추가
            for i in range(len(binary) - 1, -1, -1):
                if binary[i] == '0':
                    binary[i] = '1'
                    binary[i + 1] = '0'
                    break
            answer.append(int(''.join(binary), 2))

    return answer
  </li>
  <li>
    <b>9. 스킬 트리</b><br><br>
    <img src="https://github.com/user-attachments/assets/4f3ca9de-1e92-43ea-a8ac-3acec94a22c4" width="1000"><br><br>
    
    def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_order = list(skill)

        for s in skill_tree:
            if s in skill_order:
                if s == skill_order[0]:
                    skill_order.pop(0)  # 올바른 순서대로 배우면 제거
                else:
                    break  # 순서가 맞지 않으면 중단
        else:
            # 정상적으로 모든 문자를 확인한 경우
            answer += 1

    return answer
  </li>
  <li>
    <b>10. 줄 서는 방법</b><br><br>
    <img src="https://github.com/user-attachments/assets/a4b0b0aa-e2a1-4bf3-841e-b8b87fff9d23" width="1000"><br><br>

    import math
    
    def solution(n, k):
        answer = []
        numbers = list(range(1, n + 1))  # 1부터 n까지의 숫자 리스트
        k -= 1  # 인덱스 보정을 위해 k를 0-based로 변환
    
        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)  # (i-1)! 계산
            index = k // fact  # 현재 자릿수에 해당하는 숫자의 인덱스
            answer.append(numbers.pop(index))  # 해당 숫자를 결과에 추가
            k %= fact  # 남은 순열 인덱스 갱신
    
        return answer

  </li>
  <li>
    <b>11. 타겟 넘버</b><br><br>
    <img src="https://github.com/user-attachments/assets/d49f220a-d382-4645-abe1-e00249f03dc1" width="1000"><br><br>
    
    def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0

        # 현재 숫자를 더하거나 빼는 두 가지 선택
        return dfs(index + 1, current_sum + numbers[index]) + dfs(index + 1, current_sum - numbers[index])

    return dfs(0, 0)
  </li>
  <li>
    <b>12. 여행 경로</b><br><br>
    <img src="https://github.com/user-attachments/assets/b20aa6c6-757d-4ff5-bf5c-30aee0d71ed3" width="1000"><br><br>

    def solution(tickets):
    from collections import defaultdict

    def dfs(route):
        if len(route) == len(tickets) + 1:
            return route

        last_airport = route[-1]
        if last_airport in graph:
            for i, next_airport in enumerate(graph[last_airport]):
                if not visited[last_airport][i]:
                    visited[last_airport][i] = True
                    result = dfs(route + [next_airport])
                    if result:
                        return result
                    visited[last_airport][i] = False

        return None

    # 그래프 초기화
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)

    # 정렬
    for airport in graph:
        graph[airport].sort()

    # 방문 체크 배열 생성
    visited = {airport: [False] * len(graph[airport]) for airport in graph}

    # DFS 수행
    return dfs(["ICN"])
  </li>
  <li>
    <b>13. 네트워크</b><br><br>
    <img src="https://github.com/user-attachments/assets/edc54258-d123-437e-aebc-262a8702def9" width="1000"><br><br>

    def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    visited = [False] * n
    network_count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            network_count += 1

    return network_count
  </li>
  <li>
    <b>14. 괄호 변환</b><br><br>
    <img src="https://github.com/user-attachments/assets/a473a65f-03e9-402a-80bc-9cabfd3da91f" width="1000"><br><br>

    def solution(p):
    # 균형잡힌 괄호 문자열 분리
    def split_balanced(s):
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                return s[:i + 1], s[i + 1:]

    # 올바른 괄호 문자열 확인
    def is_correct(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    # 변환 함수
    def transform(s):
        if not s:
            return ""
        u, v = split_balanced(s)
        if is_correct(u):
            return u + transform(v)
        else:
            return '(' + transform(v) + ')' + ''.join('(' if c == ')' else ')' for c in u[1:-1])

    return transform(p)
  </li>
  <li>
    <b>15. 단어 변환</b><br><br>
    <img src="https://github.com/user-attachments/assets/4fce0a9a-01d3-4c8a-862a-46b48a5cf07b" width="1000"><br><br>

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
  </li>
</ul>
