"""
배열을 활용한 Complete Binary Tree 구축 및 순회
"""

def get_left_idx(idx:int)->int:
    return 2*idx + 1

def get_right_idx(idx:int)->int:
    return 2*idx + 2

def preorder(tree:list, cur_idx:int, result:str=""):
    result += f"{tree[cur_idx]} "

    left_idx = get_left_idx(cur_idx)
    right_idx = get_right_idx(cur_idx)

    if left_idx < len(tree):
        result = preorder(tree, left_idx, result)
    if right_idx < len(tree):
        result = preorder(tree, right_idx, result)
    
    return result

def inorder(tree:list, cur_idx:int, result:str=""):
    
    left_idx = get_left_idx(cur_idx)
    right_idx = get_right_idx(cur_idx)

    if left_idx < len(tree):
        result = inorder(tree, left_idx, result)

    result += f"{tree[cur_idx]} "

    if right_idx < len(tree):
        result = inorder(tree, right_idx, result)
    
    return result

def postorder(tree:list, cur_idx:int, result:str=""):
    left_idx = get_left_idx(cur_idx)
    right_idx = get_right_idx(cur_idx)

    if left_idx < len(tree):
        result = postorder(tree, left_idx, result)
    if right_idx < len(tree):
        result = postorder(tree, right_idx, result)
    
    result += f"{tree[cur_idx]} "
    
    return result

def solution(nodes:list[int]):
    result = []

    result.append(preorder(nodes, cur_idx=0))
    result.append(inorder(nodes, cur_idx=0))
    result.append(postorder(nodes, cur_idx=0))

    return result

if __name__ == "__main__":
    nodes = [1,2,3,4,5,6,7]

    result = solution(nodes)

    print(result)