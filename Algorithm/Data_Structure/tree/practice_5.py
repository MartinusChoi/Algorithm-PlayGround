"""
핵심 아이디어
    - 최단 경로 : BFS (너비 우선 탐색) 방식으로 탐색하면 자연스럽게 최단 경로를 찾을 수 있음
        - 이유 : 너비 우선 탐색은 현재 단계에서 가능한 모든 경로를 가보는 것!
            - 즉, 같은 단계의 탐색 경로에서 같은 값을 가지도록 경로 수를 더해가면 모든 경우의 수를 동시에 찾은 효과를 얻음
            - 자연스럽게 최단 경로가 찾아짐
        - 다만, 이미 지나친 곳을 가지 않아야 최단 경로가 되므로, 방문 여부를 크기가 같은 행렬로 관리
    - 레버칸을 지나기 전과 후가 다르게 관리되어야함! (지나기 전에 밟은 곳은 지난 후 다시 밟아서 탈출구로 향할 수 있으므로)
        - Flag를 두어 전과 후 다르게 관리되도록 행렬에 1차원 더 깊이를 생성
    - 방문 경로를 queue로 관리
        - 먼저 지나갈 경로를 먼저 처리할 수 있음
"""

from typing import List, Tuple
from collections import deque

def get_start_end_cord(maps:List[str], max_x:int, max_y:int)->Tuple[int]:
    """
    시작/종료점의 idx를 반환하는 함수
    """

    for i in range(max_y):
        for j in range(max_x):
            if maps[i][j] == "S":
                start_x = j
                start_y = i
            elif maps[i][j] == "E":
                end_x = j
                end_y = i
    
    return start_x, start_y, end_x, end_y

def is_valid_move(
    maps:List[str],
    pos_x:int,
    pos_y:int,
    max_x:int,
    max_y:int
) -> bool:
    """
    이동할 좌표가 이동이 가능한 좌표인지 검사

    1. 미로 내의 좌표이면서
    2. 좌표가 "X"로 표시되어 이동이 불가능하면 안됨
    """
    return (0 <= pos_x < max_x) and (0<= pos_y < max_y) and (maps[pos_y][pos_x] != "X")

def is_visited(
    visit_history:List[List[List[bool]]],
    pos_x:int,
    pos_y:int,
    is_after_lev:int  
)->bool:
    """
    이동할 좌표가 이미 방문한 좌표인지 검사
    lever 좌표 방문 전/후로 밟는 경로를 따로 관리하기 위해 is_after_lev로 접근
    """
    return visit_history[pos_y][pos_x][is_after_lev]

def add_to_route(
    route:deque,
    visit_history:List[List[List[bool]]],
    pos_x:int,
    pos_y:int,
    is_after_lev:int,
    time:int
):
    """
    다음 이동할 노드를 route라는 queue에 저장.
    이동할 노드가 이미 방문한 노드이면 추가하지 않음.
    is_after_lev 변수로 lever 좌표 방문 전/후로 방문 기록 따로 관리

    경로에 추가하면서 time을 증가 -> 자연스럽게 최단 경로를 추적
    """
    if not is_visited(visit_history, pos_x, pos_y, is_after_lev):
        # queue에 추가 (time 증가)
        visit_history[pos_y][pos_x][is_after_lev] = True
        route.append((pos_x, pos_y, is_after_lev, time+1))
        return route


def solution(maps:List[str]) -> int:
    """
    레버를 경유하는 가장 짧은 이동 시간을 계산하는 함수
    """
    # 다음 지나갈 경로를 저장할 queue
    # 경로 관리 객체 형태 : (pos_x, pos_y, is_after_lev, time)
    route = deque()

    # 최대 좌표 한계 설정
    max_x = len(maps[0])
    max_y = len(maps)

    # 방문 여부 관리 tensor
    visit_history = [[[False for _ in range(2)] for _ in range(max_x)] for _ in range(max_y)]

    # 시작/종료 idx 계산
    start_x, start_y, end_x, end_y = get_start_end_cord(maps, max_x, max_y)

    # 시작점을 큐에 저장
    route.append((start_x, start_y, 0, 0))
    visit_history[start_y][start_x][0] = True

    # 이동 편차 설정
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    # 다음 지나갈 경로가 남아있는 동안 반복
    while route:
        cur_x, cur_y, is_after_lev, time = route.popleft()

        # lever를 지난 후, 종료 포인트에 도달 시 지금까지 걸린 시간 반환하며 종료
        if (cur_x == end_x) and (cur_y == end_y) and (is_after_lev == 1):
            return time
        

        # 모든 방향에 대해 수행
        for dir in range(4):
            next_x = cur_x + dx[dir]
            next_y = cur_y + dy[dir]

            # 다음 이동 좌표가 이동이 가능한 좌표인지 검사
            # 이동 불가능한 좌표이면 다음 방향에 대해 수행
            if not is_valid_move(maps, next_x, next_y, max_x, max_y):
                continue
            
            # 다음 방문할 노드를 큐에 추가, 이미 방문한 좌표이면 추가하지 않음
            # 현재 방문한 노드가 Lever 노드이면 is_after_lev=1로 변경하여 이후로 다른 방문 기록 관리
            if maps[cur_y][cur_x] == "L":
                add_to_route(route, visit_history, next_x, next_y, 1, time)
            else:
                add_to_route(route, visit_history, next_x, next_y, is_after_lev, time)
        
    # 종료 지점 혹은 Lever노드에 도착하지 못했을 때
    return -1


    
if __name__ == "__main__":
    # maps = [
    #     "SOOOL",
    #     "XXXXO",
    #     "OOOOO",
    #     "OXXXX",
    #     "OOOOE"
    # ]

    maps = [
        "LOOXS",
        "OOOOX",
        "OOOOO",
        "OOOOO",
        "EOOOO"
    ]

    print(solution(maps))
