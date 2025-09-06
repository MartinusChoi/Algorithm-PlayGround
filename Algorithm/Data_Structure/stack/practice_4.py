def solution(s: str):
    stack = []

    for char in s:
        if len(stack) == 0: stack.append(char)
        else:
            if stack[-1] == char: stack.pop()
            else: stack.append(char)
    
    if len(stack) == 0: return 1
    else: return 0