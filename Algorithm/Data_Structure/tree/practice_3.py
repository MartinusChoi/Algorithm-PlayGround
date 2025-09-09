"""
Programmers: 2017 팁스타운 문제 > 예상 대진표

핵심 아이디어
    - 2의 지수로 입력되므로, 우선 leaf를 제외한 모든 node의 data가 None인 이진 트리 구축
        - leaf 이상에는 N-1개의 노드가 존재
    - 각 노드에서 parent가 같은 지 검사
        - 같으면 붙은것
        - 다르면 각각 Parent로 이동

주의:
    - none으로 구성을 노드들을 단순 복사로 구현하면 안됨 (주소가 같아져서 parent간 비교시 무조건 같은 부모로 인식)
"""

from enum import Enum

class Direction(Enum):
    PARENT = "parent"
    LEFT = "left"
    RIGHT = "right"

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_left(self, parent:Node, child:Node):
        parent.left = child
    
    def insert_right(self, parent:Node, child:Node):
        parent.right = child
    
    def insert_parent(self, parent:Node, child:Node):
        child.parent = parent
    
    def insert(self, parent:Node, child:Node, direction:Direction):
        if direction == Direction.LEFT:
            self.insert_left(parent, child)
        elif direction == Direction.RIGHT:
            self.insert_right(parent, child)
        elif direction == Direction.PARENT:
            self.insert_parent(parent, child)
    
    def left_child(self, idx:int)->int:
        return 2*idx+1
    
    def right_child(self, idx:int)->int:
        return 2*idx+2
    
    def build_tree(self, N):
        self.N = N
        self.nodes = [Node(None) for _ in range(N-1)] 

        self.nodes += [Node(value+1) for value in range(N)]

        self.root = self.nodes[0]

        for idx in range(len(self.nodes)):
            left_idx = self.left_child(idx)
            right_idx = self.right_child(idx)
            if left_idx < len(self.nodes):
                self.insert(self.nodes[idx], self.nodes[self.left_child(idx)], Direction.PARENT)
                self.insert(self.nodes[idx], self.nodes[self.left_child(idx)], Direction.LEFT)
            if right_idx < len(self.nodes):
                self.insert(self.nodes[idx], self.nodes[self.right_child(idx)], Direction.PARENT)
                self.insert(self.nodes[idx], self.nodes[self.right_child(idx)], Direction.RIGHT)
        

    def get_match_rounds(self, A:int, B:int):
        node_a = self.nodes[-(self.N-A+1)]
        node_b = self.nodes[-(self.N-B+1)]


        round = 1

        while node_a.parent != node_b.parent:
            node_a = node_a.parent
            node_b = node_b.parent
            round += 1
        
        return round

def solution(N:int, A:int, B:int):
    tree = BinaryTree()
    tree.build_tree(N)

    round = tree.get_match_rounds(A, B)

    return round

if __name__ == "__main__":
    N=8
    A=4
    B=7

    print(solution(N, A, B))