"""
객체 참조를 활용한 Binary Search Tree 구축 및 탐색
"""

from enum import Enum

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, cur_node:Node, value:int):
        if self.root == None:
            self.root = Node(value)
        elif value < cur_node.data:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self.insert(cur_node.left, value)  
        elif value >= cur_node.data:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self.insert(cur_node.right, value)
    
    def build_tree(self, values:list[int]):
        for value in values:
            self.insert(self.root, value)
    
    def search_value(self, cur_node:Node, value:int, found:bool=False)->bool:
        if cur_node == None:
            return found
        elif value == cur_node.data:
            found=True
            return found
        elif value < cur_node.data:
            return self.search_value(cur_node.left, value, found)
        elif value > cur_node.data:
            return self.search_value(cur_node.right, value, found)
    
    def search_values(self, values:list[int])->list[bool]:
        result = []

        for value in values:
            result.append(self.search_value(self.root, value))
        
        return result
    

def solution(lst, search_lst):
    bst = BinarySearchTree()
    bst.build_tree(lst)

    result = bst.search_values(search_lst)

    return result

if __name__ == "__main__":
    # lst = [5,3,8,4,2,1,7,10]
    # search_lst = [1,2,5,6]

    lst = [1,3,5,7,9]
    search_lst = [2,4,6,8,10]

    result = solution(lst, search_lst)

    print(result)