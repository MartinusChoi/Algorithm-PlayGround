"""
핵심 아이디어
    - 최소 비용으로 모든 노드를 연결한다는 것은, 어떤 노드를 루트로 하든 최소 비용이므로 -> 모든 노드의 루트가 동일할 때 까지 Union연산 수행
    - 다만, 최소 비용으로 수행해야하므로, 비용 기준 오름차순으로 정렬하여, 루트 노드가 다른 시점마다 새로운 간선에 대한 비용을 누적 연산
        - 이를 위해서는 유니온-파인드 알고리즘 구현이 필요하며, 효율성을 위해 rank 개념 도임 필요
    - rank는 루트 기준으로 측정하며, 서로 같은 rank가 등장할떄마다 1씩 늘리면서 추적함
"""

from typing import List

def find(_map:List[int], elem:int) -> int:
    cur_node = elem
    parent = _map[elem]

    while cur_node != parent:
        cur_node = parent
        parent = _map[cur_node]
    
    return cur_node

def union(_map:List[int], rank:List[int], elem_a:int, elem_b:int):
    root_a = find(_map, elem_a)
    root_b = find(_map, elem_b)

    if rank[root_a] < rank[root_b]:
        _map[root_a] = root_b
    elif rank[root_b] < rank[root_a]:
        _map[root_b] = root_a
    else:
        rank[root_a] += 1
        _map[root_b] = root_a
    

def solution(n:int, costs:List[List[int]]) -> int:
    costs = sorted(costs, key=lambda x:x[2])

    _map = [node for node in range(n)]
    rank = [0 for _ in range(n)]

    mean_cost = 0

    for cost in costs:
        node_a, node_b, weight = cost[0], cost[1], cost[2]

        if find(_map, node_a) != find(_map, node_b):
            union(_map, rank, node_a, node_b)
            mean_cost += weight
    
    return mean_cost
        
if __name__ == "__main__":
    n = 4
    costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

    print(solution(n, costs))