def solution(brown, yellow):
    width = 1

    while True:
        height = (brown+4 - 2*width) // 2
        if (width-2) * (height-2) == yellow:
            break
        width += 1
        
    return [max(width, height), min(width, height)]