from collections import deque

def solution(progresses:list, speeds:list) -> list:
    distrib_per_day = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    

    while len(progresses) > 0:
        for _ in range(len(progresses)):
            progress, speed = progresses.popleft(), speeds.popleft()
            progresses.append(progress+speed)
            speeds.append(speed)
        
        day_distrib = 0
        while (progresses) and (progresses[0] >= 100):
            progresses.popleft(), speeds.popleft()
            day_distrib += 1
        if day_distrib > 0: distrib_per_day.append(day_distrib)
    
    return distrib_per_day