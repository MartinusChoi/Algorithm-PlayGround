def solution(dirs:int) -> int:
    cur_pos = (0,0)
    unique_len = 0
    routes = []
    numeric_dirs = []

    for dir in dirs:
        if dir == 'U' : numeric_dirs.append((0,1))
        elif dir == 'D' : numeric_dirs.append((0,-1))
        elif dir == 'R' : numeric_dirs.append((1,0))
        elif dir == 'L' : numeric_dirs.append((-1,0))
    
    for dir in numeric_dirs:
        next_pos = (cur_pos[0]+dir[0], cur_pos[1]+dir[1])
        if ((-5<=next_pos[0]) & (next_pos[0]<=5)) and ((-5<=next_pos[1]) & (next_pos[1]<=5)):
            cur_route_fwd = cur_pos + next_pos
            cur_route_bwd = next_pos + cur_pos

            if (cur_route_fwd not in routes) & (cur_route_bwd not in routes) : 
                unique_len += 1

                routes.append(cur_route_fwd)
                routes.append(cur_route_bwd)
            
            cur_pos = next_pos
    
    return unique_len