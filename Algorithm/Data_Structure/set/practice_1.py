"""
핵심 아이디어:
    - 노드 번호를 사용하지 않으므로, 단순히 배열의 인덱스를 노드 번호로 사용 (0부터 시작)
    - find 연산을 재귀를 사용하지 않도록 구현
"""

from typing import List, Any

def get_initial_disjoint_set(k:int):
    """
    상호배타적 집합을 나타내는 배열에서 모든 노드를 루트로 지정하여 초기 상태로 반환합니다.
    """
    return [node for node in range(k)]

def find(disjoint_set:List[int], x:int):
    cur_node = x
    parent = disjoint_set[cur_node]

    while cur_node != parent:
        cur_node = disjoint_set[cur_node]
        parent = disjoint_set[cur_node]
    
    return cur_node

def union(disjoint_set:List[int], x:int, y:int) -> List[int]:
    """
    두 노드가 속합 집합의 union 연산을 수행합니다.
    """
    root_x = find(disjoint_set, x)
    root_y = find(disjoint_set, y)

    disjoint_set[root_y] = root_x

    return disjoint_set

def get_num_of_set(disjoint_set:List[int]):
    max_root = 0

    for cur_node, parent in enumerate(disjoint_set):
        if cur_node == parent:
            max_root += 1
    
    return max_root

def solution(k:int, operations:List[Any]) -> int:
    disjoint_set = get_initial_disjoint_set(k)

    for operation in operations:
        if operation[0] == 'u':
            disjoint_set = union(disjoint_set, operation[1], operation[2])
    
    return get_num_of_set(disjoint_set)

if __name__ == "__main__":
    # k = 3
    # operations = [['u', 0, 1], ['u', 1, 2], ['f', 2]]

    k = 4
    operations = [['u', 0, 1], ['u', 2, 3], ['f', 0]]

    print(solution(k, operations))