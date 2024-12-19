# 1week(0907)

### 강의 내용

<a href="https://velog.io/@davin0706/Ecole-%EC%BA%A1%EC%8A%A4%ED%86%A4-%EB%94%94%EC%9E%90%EC%9D%B8-1%EC%A3%BC%EC%B0%A8" target="_blank">
<img src="https://github.com/user-attachments/assets/cb1e20ab-0c40-492c-97eb-7aca11a56260" width="800"><br>
Click here to move!</a>

### La Piscine

<ul>
  <li>
    <b>1. 교점에 별 만들기</b><br><br>
    <img src="https://github.com/user-attachments/assets/784e4d8a-e504-4f29-bb74-377247ab767b" width="800"><br><br>
    
    def solution(line):
        import math
    
        # 교점 좌표를 저장할 리스트
        points = []
    
        # 직선끼리 교점 구하기
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                A, B, E = line[i]
                C, D, F = line[j]
    
                # 교점이 존재하는 조건: AD - BC != 0
                denominator = A * D - B * C
                if denominator == 0:
                    continue
    
                # x, y 좌표 계산
                x = (B * F - E * D) / denominator
                y = (E * C - A * F) / denominator
    
                # 정수 좌표만 고려
                if x == int(x) and y == int(y):
                    points.append((int(x), int(y)))
    
        # 교점 중 최대, 최소값 구하기
        min_x = min(points, key=lambda p: p[0])[0]
        max_x = max(points, key=lambda p: p[0])[0]
        min_y = min(points, key=lambda p: p[1])[1]
        max_y = max(points, key=lambda p: p[1])[1]
    
        # 격자 크기 계산
        width = max_x - min_x + 1
        height = max_y - min_y + 1
    
        # 격자 초기화
        grid = [['.'] * width for _ in range(height)]
    
        # 교점 위치 표시
        for x, y in points:
            grid[max_y - y][x - min_x] = '*'
    
        # 격자를 문자열로 변환하여 반환
        return [''.join(row) for row in grid]
    
    # 테스트 실행
    line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    result = solution(line)
    for row in result:
        print(row)
  </li>
  <li></li>
</ul>
