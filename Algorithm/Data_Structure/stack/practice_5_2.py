def solution(prices:list) -> list:
    result = [0] * len(prices)
    stack = []

    for cur_idx, cur_val in enumerate(prices):
        if cur_idx == 0 : stack.append(cur_idx)
        else:
            if prices[stack[-1]] <= cur_val: stack.append(cur_idx)
            else:
                while(prices[stack[-1]] > cur_val):
                    top_idx = stack.pop()
                    result[top_idx] = cur_idx - top_idx
                    if len(stack) == 0: break
                stack.append(cur_idx)
    
    while(len(stack)>0):
        top_idx = stack.pop()
        result[top_idx] = (len(prices) - top_idx - 1)

    return result