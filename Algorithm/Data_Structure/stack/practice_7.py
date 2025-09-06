def execute_cmd(cmd:str, trash_can:list, up:list, down:list, cursor:int, n:int) -> tuple:
    if cmd.startswith("U") : 
        for _ in range(int(cmd.split()[1])): cursor = up[cursor]

    elif cmd.startswith("D") :
        for _ in range(int(cmd.split()[1])): cursor = down[cursor]

    elif cmd == "C":
        trash_can.append(cursor-1)
        up[down[cursor]] = up[cursor]
        down[up[cursor]] = down[cursor]
        cursor = up[cursor] if n < down[cursor] else down[cursor]

    elif cmd == "Z":
        restored = trash_can.pop()+1
        up[down[restored]] = restored
        down[up[restored]] = restored
    
    return trash_can, up, down, cursor

def solution(n, k, cmd):
    trash_can = []
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+1)]
    cursor = k+1
    is_removed = ["O"] * n

    for cmd_line in cmd:
        trash_can, up, down, cursor = execute_cmd(
            cmd = cmd_line,
            trash_can=trash_can,
            up=up,
            down=down,
            cursor=cursor,
            n=n
        )
    
    while len(trash_can) > 0 : is_removed[trash_can.pop()] = "X"

    return "".join(is_removed)