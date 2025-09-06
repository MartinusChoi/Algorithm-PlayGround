def solution(N:int)->str:
    stack = []
    result = ''

    while N > 0:
        stack.append(N%2)
        N //= 2
    
    while len(stack) > 0:
        result += str(stack.pop())
    
    return result