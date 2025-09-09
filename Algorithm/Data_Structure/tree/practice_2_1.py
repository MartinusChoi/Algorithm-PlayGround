"""
배열을 활용한 Binary Search Tree 구축 및 탐색
"""

class BinarySearchTree:
    def __init__(self):
        self.tree = [None] * 1000000
    
    def left_idx(self, idx:int)->int:
        return 2*idx+1

    def right_idx(self, idx:int)->int:
        return 2*idx+2
    
    def insert(self, value:int, cur_idx:int=0)->None:
        if not self.tree[cur_idx]:
            self.tree[cur_idx] = value
        elif self.tree[cur_idx] > value:
            self.insert(value, self.left_idx(cur_idx))
        elif self.tree[cur_idx] <= value:
            self.insert(value, self.right_idx(cur_idx))

    def build_tree(self, values:list):
        for value in values:
            self.insert(value)
        
    def search_value(self, value:int, cur_idx:int=0, result:bool=False)->bool:
        if self.tree[cur_idx] == value:
            result=True
            return result
        elif self.tree[cur_idx] == None:
            return result
        elif self.tree[cur_idx] > value:
            result = self.search_value(value, self.left_idx(cur_idx), result)
        elif self.tree[cur_idx] < value:
            result = self.search_value(value, self.right_idx(cur_idx), result)
        
        return result
    
    def search_values(self, values:list[int])->list[bool]:
        result = []

        for value in values:
            result.append(self.search_value(value))
        
        return result

def solution(lst:list[int], search_lst:list[int]):
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