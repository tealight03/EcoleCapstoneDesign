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