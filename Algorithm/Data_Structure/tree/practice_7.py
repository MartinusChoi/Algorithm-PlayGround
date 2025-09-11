"""
핵심 아이디어
    - x좌표는 binary search tree 구축 요령과 같이 해당 노드를 left / right 중 어느 위치에 두어야 할 지 결정하기 위해서 사용
    - y좌표는 같은 y좌표에 해당하는 노드들이 같은 깊이를 가진다고 설명했으므로, 
        - y좌표가 같은 노드들 끼리 모으면 같은 레벨에 존재하는 노드에 집중해서 tree에 삽입할 수 있어 해당 깊이까지 찾아가 x좌표를 기준으로 left/right만 결정해 삽입
        - 부모 노드의 y좌표가 무조건 높다고 설명하고 있으므로, 등장한 모든 y좌표를 내림차순 정렬하면 제일 위의 노드부터 레벨 별로 노드를 추가 가능
주의
    - 순회를 재귀로 풀이 시 recursion을 10**6으로 늘려줘야 성공가능
    - 비재귀로 푸는 연습이 필요 (전위, 후위 순회)
"""

from typing import Dict, List, Tuple, Literal
# import sys
# sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, y_top_down:List[int], nodes_per_level:Dict[int, Tuple[int]]):
        # root 노드 초기화
        self.root = None

        # 순회 결과 리스트
        self.result = [[], []]

        # binary tree 구축
        self._build(y_top_down, nodes_per_level)

        # 전위/후위 순회 결과 저장 (재귀)
        # self._preorder(self.root)
        # self._postorder(self.root)

        # 전위/후위 순회 결과 저장 (비재귀)
        self.result[0].extend(self._traversal(type='preorder'))
        self.result[1].extend(self._traversal(type='postorder'))
    
    def _build(self, y_top_down:List[int], nodes_per_level:Dict[int, Tuple[int]]):
        """
        노드 정보에 따라 위에서부터 아래로 트리를 구축하는 함수
        """

        for level in y_top_down:
            # root가 비었으면 최상단 노드를 root로 설정
            if not self.root:
                top_node = nodes_per_level[level][0]
                x, y, val = top_node[0], top_node[1], top_node[2]
                self.root = Node(
                    x=x,
                    y=y,
                    val=val
                )
            else:
                # 같은 깊이의 노드들을 반환
                nodes_in_same_level = nodes_per_level[level]
                self._add_node_per_level(nodes_in_same_level)

    def _add_node_per_level(self, nodes_in_same_level:List[Tuple[int]]) -> None:
        """
        같은 레벨에 존재하는 노드 정보들을 입력받아 이진 트리의 올바른 곳에 위치시키는 함수.
        """
        for node in nodes_in_same_level:
            x, y, val = node[0], node[1], node[2]
            cur_node = self.root
            while True:
                if x < cur_node.x :
                    if (y < cur_node.y) and (cur_node.left == None):
                        cur_node.left = Node(
                            x=x,
                            y=y,
                            val=val
                        )
                        break                   
                    else:
                        cur_node = cur_node.left
                else:
                    if (y < cur_node.y) and (cur_node.right == None):
                        cur_node.right = Node(
                            x=x,
                            y=y,
                            val=val
                        )
                        break
                    else:
                        cur_node = cur_node.right

    def _traversal(self, type:Literal['preorder', 'postorder']) -> List[int]:
        """
        전위/후위 순회 결과를 반환하는 함수
        """
        result = []

        if type == "preorder":
            stack = [self.root]

            while stack:
                cur_node = stack.pop()

                result.append(cur_node.val)

                if cur_node.right:
                    stack.append(cur_node.right)
                
                if cur_node.left:
                    stack.append(cur_node.left)

        elif type == "postorder":
            stack = [(self.root, False)]

            while stack:
                node, visited = stack.pop()

                if node is None:
                    continue

                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))

        return result
    
    def _preorder(self, node:Node):
        """
        전위 순회 결과를 반환하는 함수
        """
        self.result[0].append(node.val)

        if node.left:
            self._preorder(node.left)
        
        if node.right:
            self._preorder(node.right)
        
        return
    
    def _postorder(self, node:Node):
        """
        후위 순회 결과를 반환하는 함수
        """
        if node.left:
            self._postorder(node.left)
        
        if node.right:
            self._postorder(node.right)
        
        self.result[1].append(node.val)
        
        return


def get_nodes_per_level(nodeinfo:List[List[int]]) -> Dict[int, Tuple[int]]:
    """
    nodeinfo를 입력받아 같은 y좌표값 (level)에 존재하는 노드별로 묶은 dict 반환
    """
    result = {}
    for idx, pos in enumerate(nodeinfo):
        x, y = pos[0], pos[1]
        if y not in result.keys():
            result[y] = [(x, y, idx+1)]
        else:
            result[y].append((x, y, idx+1))
    
    return result


def solution(nodeinfo:List[List[int]]) -> List[List[int]]:
    """
    nodeinfo에 기재된 정보에 따라 이진 트리를 구성하고, 전위/후위 순회 결과를 반환하는 함수.

    Args:
        - nodeinfo : 노드들의 2차원 좌표 정보가 1번 노드부터 차례대로 들어있는 리스트

    Return:
        - 전위 순회, 후위 순회 결과를 각각 리스트에 담아 하나의 리스트로 반환
    """
    # 같은 레벨의 노드들을 묶어 저장한 dict 계산
    nodes_per_level = get_nodes_per_level(nodeinfo)

    # 트리를 위에서부터 구성할 수 있도록 node의 y값(level)을 내림차순으로 정렬한 리스트 가져오기
    y_top_down = sorted(list(nodes_per_level.keys()), reverse=True)

    tree = BinaryTree(y_top_down, nodes_per_level)

    return tree.result

if __name__ == "__main__":
    nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

    result = solution(nodeinfo)

    print(result)