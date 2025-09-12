"""
핵심 아이디어:
    - 같은 전화번호가 입력되지 않으므로, 같은 길이를 가진 번호 단위로 끊어서 그 이후의 번호만 비교
    - 현재 전화번호의 집합에서 이후 전화번호를 현재 전화번호 길이까지 자른 것의 집합을 차집합한 결과가 현재 전화번호 집합과 다르면,
        - 이후 전화번호 의 접두어로 현재 전화번호가 존재해 빠진것이므로 False 반환
        - for 문으로 비교하는 것에 비해 효율적으로 동작함
"""

from typing import List

def solution(phone_book:List[str]) -> bool:
    phone_book = sorted(phone_book, key=lambda x:len(x))

    prev_len = len(phone_book[0])
    partisions = []
    for idx, phone_num in enumerate(phone_book):
        cur_len = len(phone_num)
        if prev_len != cur_len:
            partisions.append(idx)
        prev_len = cur_len

    window_left = 0
    for window_right in partisions:
        prefix = set(phone_book[window_left:window_right])
        prefix_len = len(phone_book[window_left])
        phone_nums = set(map(lambda x:x[:prefix_len], phone_book[window_right:]))
        if len(prefix - phone_nums) != len(prefix):
            return False
        window_left = window_right
    
    return True

def solution(phone_book:List[str]) -> bool:
    phone_book.sort() # 숫자를 기준으로 정렬

    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True

if __name__ == "__main__":
    # phone_book = ["119", "97674223", "1195524421"]
    # phone_book = ["123","456","789"]
    phone_book = ["12","123","1235","567","88"]

    print(solution(phone_book))