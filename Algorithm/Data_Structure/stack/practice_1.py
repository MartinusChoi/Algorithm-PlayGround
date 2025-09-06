def solution(simbols:str)->bool:
    open_stack = []

    for simbol in simbols:
        if simbol == '(':
            open_stack.append(simbol)
        else:
            if len(open_stack) == 0:
                return False
            open_stack.pop()
    
    return False if len(open_stack) > 0 else True