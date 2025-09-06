def hash(target:int, x:int) -> int:
    return target - x

def solution(arr:list, target:int) -> str:
    hash_table = {i:[] for i in range(target)}
    participates = []

    for element in arr : 
        if element < target: 
            hash_table[element].append(element)
            participates.append(element)

    for element in participates : 
        if hash_table[hash(target, element)] and hash(target, element) != element: return True
    
    return False