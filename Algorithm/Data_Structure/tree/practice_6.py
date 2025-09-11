"""
핵심 아이디어:
    - BFS는 단순히 최적 경로 변수 하나만을 관리하며 수행하지 않고,
    - 해당 단계에서의 상태 (늑대/양 수, 현재 노드, 해당 단계에서 방문할 수 있는 노드 후보) 를 저장하며, 각 단계에서의 선택을 제어할 수 있음
    - 이 문제에서는 각 노드의 위치에서 지금까지 추가한 방문 가능 노드들을 모두 시험
    - 반복 과정에서 max_sheep 변수로 최대값을 지속 갱신 (최대 값에서 지나쳐도 상관없음)
"""

from typing import List, Dict
from collections import deque

def build_tree(
    info:List[int], 
    edges:List[List[int]]
)->Dict[int, List[int]]:
    """
    각 노드 번호에 대한 자식 노드의 정보를 반환하는 tree dictionary를 반환합니다.
    """
    tree = {node_idx:[] for node_idx in range(len(info))}
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    return tree

def solution(info:List[int], edges:List[List[int]]):
    """
    현재 주어진 이진 초원에서 모을 수 있는 양의 최대 수를 반환합니다.
    """
    # 이진 트리 구축
    tree = build_tree(info, edges)

    # BFS를 활용한 최적해 구현을 위한 queue 정의
    q = deque()

    # 루트 노드를 queue에 추가
    # queue는 각 단계에서의 현재 상태를 저장합니다.
    # (현재 노드 위치, 양의 수, 늑대의 수, 방문할 수 있는 노드 집합)
    q.append((0, 1, 0, set()))

    # 양의 최대 수를 저장할 변수 선언
    max_sheep = 0

    # 더 방문할 노드가 남아있을 때까지 반복
    while q:
        cur_node, cur_sheep, cur_wolf, possible_nodes = q.popleft()

        # 양의 최대 수 최신화
        max_sheep = max(max_sheep, cur_sheep)

        # 방문 가능한 노드 집합에 현재 노드의 자식 노드들을 추가
        # 방문 조건에 부합하여 실제 방문 시 방문 가능한 노드 집합에서 제거 (중복 방문 가능성 배제)
        possible_nodes.update(tree[cur_node])

        for possible_node in possible_nodes:
            # 방문하려는 노드가 늑대일 떄,
            if info[possible_node]:
                if cur_sheep != cur_wolf + 1:
                    q.append(
                        (possible_node, cur_sheep, cur_wolf+1, possible_nodes - {possible_node})
                    )
            # 방문하려는 노드가 양일 때,
            else:
                q.append(
                    (possible_node, cur_sheep+1, cur_wolf, possible_nodes - {possible_node})
                )
    
    return max_sheep

if __name__ == "__main__":
    # info = [0,0,1,1,1,0,1,0,1,0,1,1]
    # edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

    info = [0,1,0,1,1,0,1,0,0,1,0]
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

    print(solution(info, edges))
        