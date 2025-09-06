def get_time(cur_val:int, sub_pirces:list)->int:
    stack = []

    for val in sub_pirces:
        stack.append(val)
        if stack[-1] < cur_val : return len(stack)

    return len(stack)

def solution(prices:list)->list:
    result = []

    for idx, cur_val in enumerate(prices):
        if idx == (len(prices)-1) : result.append(0)
        else: result.append(get_time(cur_val, prices[idx+1:]))
    
    return result