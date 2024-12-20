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