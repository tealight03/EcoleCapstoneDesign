def solution(record):
    dict = {}
    log = []
    record = [inst.split(' ') for inst in record]

    for inst in record :
        if (inst[0] == 'Enter') or (inst[0] == 'Change') :
            dict[inst[1]] = inst[2]

    for inst in record :
        if inst[0] == 'Enter' :
            log.append('%s님이 들어왔습니다.'%dict[inst[1]])
        elif inst[0] == 'Leave' :
            log.append('%s님이 나갔습니다.'%dict[inst[1]])

    return log