"""
객체 참조를 활용한 Comple Binary Tree 구축 및 순회
"""

from enum import Enum

class Direction(Enum):
    LEFT="left"
    RIGHT="right"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root:Node|None = None):
        self.root = root

    def insert_left(self, parent:Node, child:Node):
        parent.left=child
    
    def insert_right(self, parent:Node, child:Node):
        parent.right=child
    
    def insert(self, parent:Node, child:Node, direction:Direction):
        if direction == Direction.LEFT:
            self.insert_left(parent=parent, child=child)
        elif direction == Direction.RIGHT:
            self.insert_right(parent=parent, child=child)
    
    def get_complete_binary_tree(self, values:list):
        nodes = [Node(value) for value in values]
        
        self.root = nodes[0]

        for idx in range(len(nodes)):
            left_idx = 2*idx + 1
            right_idx = 2*idx + 2

            if left_idx < len(nodes):
                nodes[idx].left = nodes[left_idx]
            if right_idx < len(nodes):
                nodes[idx].right = nodes[right_idx]
    


def preorder_traversal(node:Node, result:str=""):
    result += f"{node.data} "

    if node.left:
        result = preorder_traversal(node.left, result)
    if node.right:
        result = preorder_traversal(node.right, result)
    
    return result

def inorder_traversal(node:Node, result:str=""):
    if node.left:
        result = inorder_traversal(node.left, result)
    
    result += f"{node.data} "

    if node.right:
        result = inorder_traversal(node.right, result)
    
    return result

def postorder_traversal(node:Node, result:str=""):
    if node.left:
        result = postorder_traversal(node.left, result)
    if node.right:
        result = postorder_traversal(node.right, result)
    
    result += f"{node.data} "

    return result


if __name__ == "__main__":
    tree = BinaryTree()
    tree.get_complete_binary_tree(values=[1,2,3,4,5,6,7])

    result = preorder_traversal(tree.root)
    print(result)
    result = inorder_traversal(tree.root)
    print(result)
    result = postorder_traversal(tree.root)
    print(result)