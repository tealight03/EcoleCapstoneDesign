def solution(k, room_number):
    assigned = {}

    def find_next_empty(room):
        if room not in assigned:
            assigned[room] = room + 1
            return room
        assigned[room] = find_next_empty(assigned[room])
        return assigned[room]

    result = []
    for room in room_number:
        result.append(find_next_empty(room))

    return result