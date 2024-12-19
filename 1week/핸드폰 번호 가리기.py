def solution(phone_number):
    # 전화번호의 뒤 4자리를 제외한 나머지를 *로 대체
    return "*" * (len(phone_number) - 4) + phone_number[-4:]