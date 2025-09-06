def make_empty_doll_stacks(N):
    doll_stacks = []

    for _ in range(N):
        doll_stacks.append([])
    
    return doll_stacks

def get_doll_stacks(board:list, N:int) -> list:
    doll_stacks = make_empty_doll_stacks(N)

    for row in board[::-1]:
        for idx, doll_val in enumerate(row):
            doll_stacks[idx].append(doll_val)
    
    return doll_stacks

def remove_empty_space(doll_stacks:list) -> list:
    
    for idx in range(len(doll_stacks)):
        while doll_stacks[idx] and doll_stacks[idx][-1] == 0 :
            doll_stacks[idx].pop()
    
    return doll_stacks

def solution(board:list, moves:list) -> int :
    N = len(board[0])
    
    doll_stacks = get_doll_stacks(board, N)
    busket = []

    removed_doll_num = 0

    doll_stacks = remove_empty_space(doll_stacks)

    for move in moves:
        if doll_stacks[move-1]:
            cur_doll = doll_stacks[move-1].pop()

            if busket and (busket[-1] == cur_doll):
                busket.pop()
                removed_doll_num += 2
            else:
                busket.append(cur_doll)
    
    return removed_doll_num