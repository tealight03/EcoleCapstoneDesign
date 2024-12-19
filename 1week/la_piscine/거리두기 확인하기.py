def solution(places):
    from collections import deque

    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def is_valid(place):
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':  # 사람이 있는 경우
                    if not bfs(i, j, place):
                        return 0
        return 1

    def bfs(x, y, place):
        queue = deque([(x, y, 0)])  # (x, y, 거리)
        visited = [[False] * 5 for _ in range(5)]
        visited[x][y] = True

        while queue:
            cx, cy, dist = queue.popleft()

            if dist > 0 and place[cx][cy] == 'P':  # 거리 안에 사람이 있는 경우
                return False

            if dist >= 2:  # 거리 2를 넘으면 검사 중단
                continue

            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                    if place[nx][ny] != 'X':  # 파티션이 아닌 경우만 이동
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist + 1))

        return True

    return [is_valid(place) for place in places]