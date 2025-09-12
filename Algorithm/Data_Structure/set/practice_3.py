"""
핵심 아이디어:
    - 각 인물의 현재 차례를 turn 변수에 저장해 차례가 지날 때마다 늘리기
    - word를 history라는 집합으로 관리하여 현재까지 나온 적 있는 단어인지 검사
    - 매 단어마다 끝단어 저장해 다음 순서때 비교
    - 사람의 번호를 반환하기 위해 사람의 번호 길이 만큼의 리스트를 만들고, idx%n으로 같은 패턴이 반복되도록 함
"""

from typing import List

def solution(n:int, words:List[str]) -> List[int]:
    nums = [num+1 for num in range(n)]
    turn = [1 for _ in range(n)]
    history = set()

    last_char = None

    for idx, word in enumerate(words):
        if ((last_char != None) and (last_char != word[0])) or (word in history):
            return [nums[idx%n], turn[idx%n]]
        last_char = word[-1]
        turn[idx%n] += 1
        history.update([word])
    
    return [0, 0]

if __name__ == "__main__":
    # n = 3
    # words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    # n = 5
    # words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    n = 2
    words = ["hello", "one", "even", "never", "now", "world", "draw"]

    print(solution(n, words))