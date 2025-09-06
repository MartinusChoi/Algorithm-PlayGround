def is_valid_string(string:str) -> bool:
    stack = []

    for char in string:
        if char in ["(", "[", "{"] : stack.append(char)
        elif len(stack) == 0 : return False
        elif (char == ")") and (stack[-1] == "(") : stack.pop()
        elif (char == "]") and (stack[-1] == "[") : stack.pop()
        elif (char == "}") and (stack[-1] == "{") : stack.pop()
    
    if len(stack) == 0: return True
    else: return False

def solution(s: str):
    valid_num = 0

    for _ in range(len(s)):
        if is_valid_string(s): valid_num += 1
        s = s[-1] + s[:-1]

    return valid_num