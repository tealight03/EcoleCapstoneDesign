from collections import deque, defaultdict

def solution(n, edge):
    # 그래프 초기화
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # BFS로 최단 거리 계산
    distances = [-1] * (n + 1)
    distances[1] = 0  # 시작 노드
    queue = deque([1])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드만
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # 가장 먼 거리의 노드 개수 계산
    max_distance = max(distances)
    return distances.count(max_distance)